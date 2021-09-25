#!/usr/bin/env python

""" MultiQC remove_duplicate plugin module """

from __future__ import print_function
from collections import OrderedDict
import logging

from multiqc import config
from multiqc.modules.base_module import BaseMultiqcModule

from .fragment_count_plot import fragment_count_plot

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):
        # Halt execution if we've disabled the plugin
        if config.kwargs.get('disable_remove_duplicate_plugin', True):
            return None

        # Initialise the parent module Class object
        super(MultiqcModule, self).__init__(
            name = 'Remove Duplicates',
            target = "remove_duplicate",
            anchor = 'remove_duplicate',
            href = 'https://github.com/hukai916/scatacseqflow/blob/main/modules/local/remove_duplicate.nf',
            info = " is a scatacseqflow module to show how many PCR duplicate fragments are removed for each sample."
        )

        # Find and load any input files for this module
        self.duplicate_summary = dict()
        for f in self.find_log_files('remove_duplicate/summary_file'):
            self.duplicate_summary[f['s_name']] = dict()
            for l in f['f'].splitlines():
                for key in ('total unique fragments:', 'total duplicate fragments:', 'other fragments(unproper mapped or with no corrected barcodes):'):
                    value = l.split(key)[1].split()[0][:-1]
                    self.duplicate_summary[f['s_name']][key] = value

        # Filter out samples matching ignored sample names
        self.duplicate_summary = self.ignore_samples(self.duplicate_summary)

        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.duplicate_summary) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning

        log.info("Found {} reports".format(len(self.duplicate_summary)))

        # Write parsed report data to a file
        self.write_data_file(self.duplicate_summary, 'multiqc_remove_duplicate')

        fragment_count_plot(self)

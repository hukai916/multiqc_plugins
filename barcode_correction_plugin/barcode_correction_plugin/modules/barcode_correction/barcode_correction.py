#!/usr/bin/env python

""" MultiQC barcode_correction plugin module """

from __future__ import print_function
from collections import OrderedDict
import logging

from multiqc import config
from multiqc.modules.base_module import BaseMultiqcModule

from .read_count_plot import read_count_plot

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):
        # Halt execution if we've disabled the plugin
        if config.kwargs.get('disable_barcode_correction_plugin', True):
            return None

        # Initialise the parent module Class object
        super(MultiqcModule, self).__init__(
            name = 'Barcode Correction',
            target = "barcode_correction",
            anchor = 'barcode_correction',
            href = 'https://github.com/hukai916/scatacseqflow/blob/main/modules/local/correct_barcode.nf',
            info = " is a scatacseqflow module to show how many barcodes are corrected for each sample."
        )

        # Find and load any input files for this module
        self.barcode_summary = dict()
        for f in self.find_log_files('barcode_correction/summary_file'):
            # note that the name can't contain "_", so that barcode_correction/summary_file is not valid key name.
            self.barcode_summary[f['s_name']] = dict()
            for l in f['f'].splitlines():
                for key in ('total valid:', 'total corrected:', 'total discarded:'):
                    value = l.split(key)[1].split()[0][:-1]
                    self.barcode_summary[f['s_name']][key] = value

        # Filter out samples matching ignored sample names
        self.barcode_summary = self.ignore_samples(self.barcode_summary)

        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.barcode_summary) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning

        log.info("Found {} reports".format(len(self.barcode_summary)))

        # Write parsed report data to a file
        self.write_data_file(self.barcode_summary, 'multiqc_barcode_correction')

        read_count_plot(self)

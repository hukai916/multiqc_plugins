#!/usr/bin/env python

""" MultiQC example plugin module """

from __future__ import print_function
from collections import OrderedDict
import logging

from multiqc import config
from multiqc.plots import linegraph
from multiqc.modules.base_module import BaseMultiqcModule

import os
from .plot_figure import plot_figure

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):

        # Halt execution if we've disabled the plugin
        if config.kwargs.get('disable_get_valid_barcode_plugin', True):
            return None

        # Initialise the parent module Class object
        super(MultiqcModule, self).__init__(
            name = 'Valid barcodes',
            target = "get_valid_barcode",
            anchor = 'get_valid_barcode',
            href = '',
            info = ""
        )
        self.get_valid_barcode = dict()

        plot_figure(self, dir_n = "get_valid_barcode", endswith = "*.jpg", img_width = "32%", name = "Valid barcodes", description = "Valid cell barcodes are inferred with 'inflection point' method as the barcode count cutoff is set to the inflection point in the plot.", helptext = "Cell barcodes in the top-left corner of the plot are valid.")

        # Filter out samples matching ignored sample names
        self.get_valid_barcode = self.ignore_samples(self.get_valid_barcode)
        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.get_valid_barcode) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning
        log.info("Found {} reports".format(len(self.get_valid_barcode)))

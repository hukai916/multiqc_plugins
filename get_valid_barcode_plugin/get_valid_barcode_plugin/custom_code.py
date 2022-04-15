#!/usr/bin/env python
""" MultiQC get_valid_barcode plugin functions

We can add any custom Python functions here and call them
using the setuptools plugin hooks.
"""

from __future__ import print_function
from pkg_resources import get_distribution
import logging

from multiqc.utils import report, util_functions, config

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

# Save this plugin's version number (defined in setup.py) to the MultiQC config
config.get_valid_barcode_plugin_version = get_distribution("multiqc_get_valid_barcode_plugin").version


# Add default config options for the things that are used in MultiQC_NGI
def get_valid_barcode_plugin_execution_start():
    """ Code to execute after the config files and
    command line flags have been parsedself.

    This setuptools hook is the earliest that will be able
    to use custom command line flags.
    """

    # Halt execution if we've disabled the plugin
    if config.kwargs.get('disable_get_valid_barcode_plugin', True):
        return None

    log.info("Running get_valid_barcode MultiQC Plugin v{}".format(config.get_valid_barcode_plugin_version))

    if 'get_valid_barcode/jpeg' not in config.sp:
        config.update_dict( config.sp, { 'get_valid_barcode/jpeg': { 'fn': '*.jpg' } } )
    print(config.sp)

    # Some additional filename cleaning
    config.fn_clean_exts.extend([
        '.my_tool_extension',
        '.removeMetoo'
    ])

    # Ignore some files generated by the custom pipeline
    config.fn_ignore_paths.extend([
        '*/my_awesome_pipeline/fake_news/*',
        '*/my_awesome_pipeline/red_herrings/*',
        '*/my_awesome_pipeline/noisy_data/*',
        '*/my_awesome_pipeline/rubbish/*'
    ])

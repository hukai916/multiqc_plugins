#!/usr/bin/env python
""" MultiQC archr plugin functions

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
config.archr_plugin_version = get_distribution("multiqc_archr_plugin").version


# Add default config options for the things that are used in MultiQC_NGI
def archr_plugin_execution_start():
    """ Code to execute after the config files and
    command line flags have been parsedself.

    This setuptools hook is the earliest that will be able
    to use custom command line flags.
    """

    # Halt execution if we've disabled the plugin
    if config.kwargs.get('disable_archr_plugin', True):
        return None

    log.info("Running ArchR MultiQC Plugin v{}".format(config.archr_plugin_version))

    # Add to the main MultiQC config object.
    # User config files have already been loaded at this point
    #   so we check whether the value is already set. This is to avoid
    #   clobbering values that have been customised by users.

    # Add to the search patterns used by modules
    if 'archr/jpeg' not in config.sp:
        config.update_dict( config.sp, { 'archr/jpeg': { 'fn': '*.jpg' } } )
    if 'archr/summary_add_doubletscores' not in config.sp:
        config.update_dict( config.sp, { 'archr/summary_add_doubletscores': { 'fn': 'summary_add_doubletscores_*.txt' } } )
    if 'archr/summary_filter_doublets' not in config.sp:
        config.update_dict( config.sp, { 'archr/summary_filter_doublets': { 'fn': 'summary_filter_doublets.txt' } } )

    # if 'archr/create_arrowfiles_fragment' not in config.sp:
    #     config.update_dict( config.sp, { 'archr/create_arrowfiles_fragment': { 'fn': '*Fragment_Size_Distribution*.jpg' } } )
    # if 'archr/create_arrowfiles_tss' not in config.sp:
    #     config.update_dict( config.sp, { 'archr/create_arrowfiles_tss': { 'fn': '*TSS_by_Unique_Frags*.jpg' } } )
    # if 'archr/add_doubletscores' not in config.sp:
    #     config.update_dict( config.sp, { 'archr/add_doubletscores': { 'fn': '*Doublet-Summary*.jpg' } } )
    # if 'archr/archrproject_qc' not in config.sp:
    #     config.update_dict( config.sp, { 'archr/archrproject_qc': { 'fn': 'QC-Sample-FragSizes-TSSProfile.jpg\|TSS-vs-Frags.jpg\|QC-Sample-Statistics.pdf' } } )
        # config.update_dict( config.sp, { 'archr/archrproject_qc': { 'fn': 'QC-Sample-FragSizes-TSSProfile.jpg' } } )

    # if 'archr/clustering' not in config.sp:
    #     config.update_dict( config.sp, { 'archr/clustering': { 'fn': '*.jpg' } } )

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

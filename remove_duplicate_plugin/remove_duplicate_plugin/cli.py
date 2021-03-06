#!/usr/bin/env python
"""
MultiQC command line options - we tie into the MultiQC
core here and add some new command line parameters.

See the Click documentation for more command line flag types:
http://click.pocoo.org/5/
"""

import click

# Sets config.kwargs['disable_plugin'] to True if specified (will be False otherwise)
disable_remove_duplicate_plugin = click.option('--disable-remove-duplicate-plugin', 'disable_remove_duplicate_plugin',
    is_flag = True,
    help = "Disable the remove_duplicate MultiQC plugin on this run"
)

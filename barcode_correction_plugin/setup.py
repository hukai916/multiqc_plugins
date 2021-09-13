#!/usr/bin/env python
"""
barcode correction plugin for scatacseqqc, plot barcode correction results.

For more information about MultiQC, see http://multiqc.info
"""

from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'multiqc_barcode_correction_plugin',
    version = version,
    author = 'Kai Hu',
    author_email = 'kai.hu@umassmed.edu',
    description = "barcode_correction MultiQC plugin",
    long_description = __doc__,
    keywords = 'bioinformatics',
    url = '',
    download_url = '',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'multiqc'
    ],
    entry_points = {
        'multiqc.modules.v1': [
            'barcode_correction = barcode_correction_plugin.modules.barcode_correction:MultiqcModule',
        ],
        'multiqc.cli_options.v1': [
            'disable_barcode_correction_plugin = barcode_correction_plugin.cli:disable_barcode_correction_plugin'
        ],
        'multiqc.hooks.v1': [
            'execution_start = barcode_correction_plugin.custom_code:barcode_correction_plugin_execution_start'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)

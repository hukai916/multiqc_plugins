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
        if config.kwargs.get('disable_archr_plugin', True):
            return None

        # Initialise the parent module Class object
        super(MultiqcModule, self).__init__(
            name = 'ArchR reports',
            target = "archr",
            anchor = 'archr',
            href = '',
            info = ""
        )

        self.archr = dict()
        # archr_create_arrowfiles_fragment:
        plot_figure(self, dir_n = "archr_create_arrowfiles/", endswith = "Fragment_Size_Distribution.jpg", img_width = "32%", name = "Arrowfile QC1: fragment size distribution.", description = "When creating ArchR arrow files, two QC metrics will be calculated, QC1 is fragement size distribution.", helptext = "To be added")
        # archr_create_arrowfiles_tss:
        plot_figure(self, dir_n = "archr_create_arrowfiles/", endswith = "TSS_by_Unique_Frags.jpg", img_width = "32%", name = "Arrowfile QC2: TSS summary.", description = "ArchR arrowfile tss for each sample.", helptext = "To be added")
        # archr_add_doubletscores:
        plot_figure(self, dir_n = "archr_add_doubletscores/", endswith = "Doublet-Summary.jpg", img_width = "32%", name = "Arrowfile doublet QC: statistics.", description = "ArchR doublet statistics for each sample.", helptext = "To be added")
        # archr_archrproject_qc:
        plot_figure(self, dir_n = "archr_archrproject_qc/", endswith = ".jpg", img_width = "32%", name = "ArchRproject QC: statistics.", description = "ArchRProject QC.", helptext = "To be added")
        # archr_clustering:
        plot_figure(self, dir_n = "archr_clustering/", endswith = ".jpg", img_width = "48%", name = "ArchRproject clusterings: statistics", description = "ArchR clusterings for each sample.", helptext = "To be added")
        # archr_embedding:
        plot_figure(self, dir_n = "archr_embedding/", endswith = ".jpg", img_width = "48%", name = "ArchR embeddings: plots", description = "ArchR embeddings.", helptext = "To be added")
        # archr_marker_gene:
        plot_figure(self, dir_n = "archr_marker_gene/", endswith = ".jpg", img_width = "48%", name = "ArchR marker gene: plots", description = "ArchR marker gene.", helptext = "To be added")
        # archr_scrnaseq_unconstrained:
        plot_figure(self, dir_n = "archr_scrnaseq_unconstrained/", endswith = ".jpg", img_width = "48%", name = "ArchR scRNA-seq unconstrained: plots", description = "ArchR scRNA-seq unconstrained.", helptext = "To be added")
        # archr_scrnaseq_constrained:
        plot_figure(self, dir_n = "archr_scrnaseq_constrained/", endswith = ".jpg", img_width = "48%", name = "ArchR scRNA-seq constrained: plots", description = "ArchR scRNA-seq constrained.", helptext = "To be added")
        # archr_get_marker_peaks_clusters:
        plot_figure(self, dir_n = "archr_get_marker_peaks_clusters/", endswith = ".jpg", img_width = "48%", name = "ArchR get marker peaks (clusters): plots", description = "ArchR get marker peaks (clusters).", helptext = "To be added")
        # archr_get_marker_peaks_clusters2:
        plot_figure(self, dir_n = "archr_get_marker_peaks_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR get marker peaks (clusters2): plots", description = "ArchR get marker peaks (clusters2).", helptext = "To be added")
        # archr_marker_peaks_in_tracks_clusters:
        plot_figure(self, dir_n = "archr_marker_peaks_in_tracks_clusters/", endswith = ".jpg", img_width = "48%", name = "ArchR marker peaks in tracks (clusters): plots", description = "ArchR marker peaks in tracks (clusters).", helptext = "To be added")
        # archr_marker_peaks_in_tracks_clusters2:
        plot_figure(self, dir_n = "archr_marker_peaks_in_tracks_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR marker peaks in tracks (clusters2): plots", description = "ArchR marker peaks in tracks (clusters2).", helptext = "To be added")
        # archr_pairwise_test_clusters:
        plot_figure(self, dir_n = "archr_pairwise_test_clusters/", endswith = ".jpg", img_width = "48%", name = "ArchR pairwise test (clusters): plots", description = "ArchR pairwise test (clusters).", helptext = "To be added")
        # archr_pairwise_test_clusters2:
        plot_figure(self, dir_n = "archr_pairwise_test_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR pairwise test (clusters2): plots", description = "ArchR pairwise test (clusters2).", helptext = "To be added")
        # archr_motif_deviations_clusters:
        plot_figure(self, dir_n = "archr_motif_deviations_clusters/", endswith = ".jpg", img_width = "48%", name = "ArchR motif deviation (clusters): plots", description = "ArchR motif deviation (clusters).", helptext = "To be added")
        # archr_motif_deviations_clusters2:
        plot_figure(self, dir_n = "archr_motif_deviations_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR motif deviation (clusters2): plots", description = "ArchR motif deviation (clusters2).", helptext = "To be added")
        # archr_coaccessibility_clusters:
        plot_figure(self, dir_n = "archr_coaccessibility_clusters/", endswith = ".jpg", img_width = "48%", name = "ArchR coaccessibility (clusters): plots", description = "ArchR coaccessibility (clusters).", helptext = "To be added")
        # archr_coaccessibility_clusters2:
        plot_figure(self, dir_n = "archr_coaccessibility_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR coaccessibility (clusters2): plots", description = "ArchR coaccessibility (clusters2).", helptext = "To be added")
        # archr_peak2genelinkage_clusters2:
        plot_figure(self, dir_n = "archr_peak2genelinkage_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR peak to gene linkage (clusters2): plots", description = "ArchR peak to gene linkage (clusters2).", helptext = "To be added")
        # archr_trajectory_clusters2:
        plot_figure(self, dir_n = "archr_trajectory_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR trajectory (clusters2): plots", description = "ArchR trajectory (clusters2).", helptext = "To be added")

        # Filter out samples matching ignored sample names
        self.archr = self.ignore_samples(self.archr)
        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.archr) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning
        log.info("Found {} reports".format(len(self.archr)))

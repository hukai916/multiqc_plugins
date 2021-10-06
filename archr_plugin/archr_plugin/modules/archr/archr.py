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
        plot_figure(self, dir_n = "archr_create_arrowfiles/", endswith = "Fragment_Size_Distribution.jpg", img_width = "32%", name = "Arrowfile QC: fragment size distribution", description = "", helptext = "For good quality data, we expect to see a periodic pattern reflecting the nucleosomal wrapping of DNA. There are valleys and hills because fragments must span integral number of nucleosomes.")
        # plot_figure(self, dir_n = "QualityControl_*/", endswith = "Fragment_Size_Distribution.jpg", img_width = "32%", name = "Arrowfile QC1: fragment size distribution.", description = "When creating ArchR arrow files, two QC metrics will be calculated, QC1 is fragement size distribution.", helptext = "To be added")
        # archr_create_arrowfiles_tss:
        plot_figure(self, dir_n = "archr_create_arrowfiles/", endswith = "TSS_by_Unique_Frags.jpg", img_width = "32%", name = "Arrowfile QC: TSS summary", description = "", helptext = "Transcription Start Site (TSS) enrichment score is a metric to evaluate the signal-to-background ratio. The rational behind is that ATAC-seq data is universally enriched at TSS sites compared to other genomic regions. <br>For good quality data, we expect to see an enrichment of read peaks around TSS regions relative to flanking regions. By default, ArchR filters out cells that have a TSS score less than 4 and fewer than 1000 unique nuclear fragments. Those cutoffs can be configured under archr_create_arrowfiles module.")
        # plot_figure(self, dir_n = "QualityControl_*/", endswith = "Fragment_Size_Distribution.jpg", img_width = "32%", name = "Arrowfile QC1: fragment size distribution.", description = "When creating ArchR arrow files, two QC metrics will be calculated, QC1 is fragement size distribution.", helptext = "To be added")
        # archr_add_doubletscores:
        # Add R^2 onto the description:
        text = ""
        for f in self.find_log_files('archr/summary_add_doubletscores'):
            file_path = os.path.join(f['root'], f['fn'])
            with open(file_path, "r") as summary:
                if "UMAP Projection R^2" in line:
                    text = text + line.strip() + "\n"
        plot_figure(self, dir_n = "archr_add_doubletscores/", endswith = "Doublet-Summary.jpg", img_width = "32%", name = "Arrowfile QC: doublet removal", description = text, helptext = "Doublet refers to a single droplet receiving a single cell barcode but more than one nucleus. It causes reads that come from more than one cells to appear as if they were from one single cell. To label those doublet, ArchR leverages a strategy that projects synthetic doublet into the UMAP embedding and finds the nearest neighbors. The doublet enrichment plot represents the enrichment of simulated doublets nearby each cell; the doublet density plot represents the density of simulated doublet projectcions.<br>ArchR reports a R^2 value for the UMAP projection (details see corresponding summary_add_doubletscores_xxx.txt). If that value is less than 0.9, we recommend skipping doublet removal or use **knnMethod = 'LSI'** and **force = TRUE**.")
        # plot_figure(self, dir_n = "doublet_qc_*/", endswith = "Doublet-Summary.jpg", img_width = "32%", name = "Arrowfile doublet QC: statistics.", description = "ArchR doublet statistics for each sample.", helptext = "To be added")
        # archr_archrproject_qc:
        plot_figure(self, dir_n = "archr_archrproject_qc/", endswith = ".jpg", img_width = "32%", name = "ArchRProject sample statistics", description = "", helptext = "This section aggregates statistics across multiple samples so that it is easier to compare important metrics across samples.")
        # archr_filter_doublets:
        text = ""
        for f in self.find_log_files('archr/summary_filter_doublets'):
            file_path = os.path.join(f['root'], f['fn'])
            line_num = 0
            with open(file_path, "r") as summary:
                for num, line in enumerate(summary):
                    if "cells from ArchRProject!" in line:
                        line_num = num
                        break
            with open(file_path, "r") as summary:
                for num, line in enumerate(summary):
                    if num >= line_num and "%)" in line:
                        text = text + line.strip() + "<br>"
        plot_figure(self, dir_n = "archr_filter_doublets/", endswith = ".jpg", img_width = "48%", name = "Filtering doublets", description = text, helptext = "Count how many doublets are filtered out.")
        # archr_clustering:
        plot_figure(self, dir_n = "archr_clustering/", endswith = ".jpg", img_width = "48%", name = "Clusterings", description = "", helptext = "ArchR provides two approaches for clustering: default method is 'Seurat', alternatively, we can also use 'Scran'.")
        # archr_embedding:
        plot_figure(self, dir_n = "archr_embedding/", endswith = ".jpg", img_width = "48%", name = "Single-cell embeddings", description = "", helptext = "ArchR provides two approaches, namely Uniform Manifold Approximation and Projection (UMAP) and t-Stocastic Neighbor Embedding (t-SNE). We plot the embedding use both methods against clusterings with either Seurat and Scran.<br>In addition, the effects of Harmony batch correction are visualized using UMAP and t-SNE (only performed for Seurat clustering).")
        # archr_marker_gene:
        plot_figure(self, dir_n = "archr_marker_gene/", endswith = ".jpg", img_width = "48%", name = "Marker genes", description = "", helptext = "Marker genes are identified based on gene scores, user supplied marker genes (via **markerGenes**) are labeled in the heatmap. Marker genes are also visualized on embeddings. To improve the visual interpretation, MAGIC is leveraged to impute the gene scores by smoothing the signals (Plot-UMAP-Marker-Genes-W-Imputation.jpeg).")
        # archr_scrnaseq_unconstrained:
        plot_figure(self, dir_n = "archr_scrnaseq_unconstrained/", endswith = ".jpg", img_width = "48%", name = "Unconstrained integration of scRNA-seq data", description = "", helptext = "To integrate matching scRNA-seq data, ArchR first performs unconstrained integration, which provides a framework for constrained integration.")
        # archr_scrnaseq_constrained:
        plot_figure(self, dir_n = "archr_scrnaseq_constrained/", endswith = ".jpg", img_width = "48%", name = "Constrained integration of scRNA-seq data", description = "", helptext = "Based on the general cell types framework according to unconstrained integration plus user supplied additional clustering information, further integration (constrained) are performed.")
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
        # archr_get_positive_tf_regulator_clusters:
        plot_figure(self, dir_n = "archr_get_positive_tf_regulator_clusters/", endswith = ".jpg", img_width = "48%", name = "ArchR positive TF regulator (clusters): plots", description = "ArchR positive TF regulator (clusters).", helptext = "To be added")
        # archr_get_positive_tf_regulator_clusters2:
        plot_figure(self, dir_n = "archr_get_positive_tf_regulator_clusters2/", endswith = ".jpg", img_width = "48%", name = "ArchR positive TF regulator (clusters2): plots", description = "ArchR positive TF regulator (clusters2).", helptext = "To be added")

        # Filter out samples matching ignored sample names
        self.archr = self.ignore_samples(self.archr)
        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.archr) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning
        log.info("Found {} reports".format(len(self.archr)))

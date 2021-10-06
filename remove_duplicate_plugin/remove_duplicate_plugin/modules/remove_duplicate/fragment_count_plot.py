"""
Modified from fastqc module: fastqc.py
"""

from multiqc.plots import bargraph

def fragment_count_plot(self):
    """Stacked bar plot showing counts of fragments"""
    pconfig = {
        "id": "remove_duplicate_counts_plot",
        "title": "Remove Duplicate: Fragment Counts",
        "ylab": "Number of fragments",
        "cpswitch_counts_label": "Number of fragments",
        "hide_zero_cats": False,
    }
    pdata = dict()

    for s_name in self.duplicate_summary:
        pdata[s_name] = dict()

        pdata[s_name]["Total Unique Fragments"] = int(self.duplicate_summary[s_name]["total unique fragments:"])
        pdata[s_name]["Total Duplicate Fragments"] = int(self.duplicate_summary[s_name]["total duplicate fragments:"])
        pdata[s_name]["Other Fragments"] = int(self.duplicate_summary[s_name]["other fragments(unproper mapped or with no corrected barcodes):"])

    pcats = ["Total Unique Fragments", "Total Duplicate Fragments", "Other Fragments"]
    pconfig["use_legend"] = False
    pconfig["cpswitch"] = False

    self.add_section(
        name="Fragment Counts",
        anchor="remove_duplicate_fragment_counts",
        description="",
        helptext="""
        This plot shows the total number of fragments, broken down into unique fragments and duplicate fragments and other fragments (not properly mapped or without valid cell barcodes).
        This plot is generated based on the summary file from the remove_duplicate module.
        For fragments that have the same cell barcode, the duplication is determined by looking at the starting coordinates and the fragment lengths. Soft-clippings are extended before comparison. Among duplicated fragments, the one with the highest mean sequencing quality will be kept.
        The number of total duplicate fragments is calculated as: the number of total fragments - the number of total fragments that have at least one count (total unique fragments) - the number of other fragments.
        """,
        plot=bargraph.plot(pdata, pcats, pconfig),
    )

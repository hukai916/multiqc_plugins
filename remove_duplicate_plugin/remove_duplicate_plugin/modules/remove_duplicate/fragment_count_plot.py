"""
Modified from fastqc module: fastqc.py
"""

from multiqc.plots import bargraph

def fragment_count_plot(self):
    """Stacked bar plot showing counts of fragments"""
    pconfig = {
        "id": "remove_duplicate_counts_plot",
        "title": "Remove Duplicate: Read Counts",
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
        This plot shows the total number of fragments, broken down into unique fragments and duplicate fragments and other fragments (unproper mapped or without corrected barcodes).
        This plot is generated based on the summary file from the scatacseqflow remove_duplicate module.
        """,
        plot=bargraph.plot(pdata, pcats, pconfig),
    )

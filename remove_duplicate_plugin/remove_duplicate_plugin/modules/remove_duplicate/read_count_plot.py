"""
Modified from fastqc module: fastqc.py
"""

from multiqc.plots import bargraph

def read_count_plot(self):
    """Stacked bar plot showing counts of reads"""
    pconfig = {
        "id": "remove_duplicate_counts_plot",
        "title": "Remove Duplicate: Read Counts",
        "ylab": "Number of reads",
        "cpswitch_counts_label": "Number of reads",
        "hide_zero_cats": False,
    }
    pdata = dict()

    for s_name in self.duplicate_summary:
        pdata[s_name] = dict()

        pdata[s_name]["Total Unique Reads"] = int(self.duplicate_summary[s_name]["total unique reads:"])
        pdata[s_name]["Total Duplicate Reads"] = int(self.duplicate_summary[s_name]["total duplicate reads:"])

    pcats = ["Total Unique Reads", "Total Duplicate Reads"]
    pconfig["use_legend"] = False
    pconfig["cpswitch"] = False

    self.add_section(
        name="Read Counts",
        anchor="remove_duplicate_read_counts",
        description="",
        helptext="""
        This plot shows the total number of reads, broken down into unique reads and duplicate reads.
        This plot is generated based on the summary file from the scatacseqflow remove_duplicate module.
        """,
        plot=bargraph.plot(pdata, pcats, pconfig),
    )

"""
Modified from fastqc module: fastqc.py
"""

from multiqc.plots import bargraph

def read_count_plot(self):
    """Stacked bar plot showing counts of reads"""
    pconfig = {
        "id": "bam_filter_counts_plot",
        "title": "Bam Filter: Read Counts",
        "ylab": "Number of reads",
        "cpswitch_counts_label": "Number of reads",
        "hide_zero_cats": False,
    }
    pdata = dict()

    for s_name in self.duplicate_summary:
        pdata[s_name] = dict()

        pdata[s_name]["Total Valid Reads"] = int(self.duplicate_summary[s_name]["total valid:"])
        pdata[s_name]["Total Filtered Reads"] = int(self.duplicate_summary[s_name]["total filtered:"])

    pcats = ["Total Valid Reads", "Total Filtered Reads"]
    pconfig["use_legend"] = False
    pconfig["cpswitch"] = False

    self.add_section(
        name="Read Counts",
        anchor="bam_filter_read_counts",
        description="",
        helptext="""
        This plot shows the total number of reads, broken down into valid reads and filtered reads.
        This plot is generated based on the summary file from the scatacseqflow bam_filter module.
        """,
        plot=bargraph.plot(pdata, pcats, pconfig),
    )

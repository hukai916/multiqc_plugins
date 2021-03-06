"""
Modified from fastqc module: fastqc.py
"""

from multiqc.plots import bargraph

def read_count_plot(self):
    """Stacked bar plot showing counts of reads"""
    pconfig = {
        "id": "barcode_read_counts_plot",
        "title": "Barcode Correction: Read Counts",
        "ylab": "Number of reads",
        "cpswitch_counts_label": "Number of reads",
        "hide_zero_cats": False,
    }
    pdata = dict()

    for s_name in self.barcode_summary:
        pdata[s_name] = dict()

        pdata[s_name]["Valid Reads"] = int(self.barcode_summary[s_name]["total valid:"])
        pdata[s_name]["Corrected Reads"] = int(self.barcode_summary[s_name]["total corrected:"])
        pdata[s_name]["Discarded Reads"] = int(self.barcode_summary[s_name]["total discarded:"])

    pcats = ["Valid Reads", "Corrected Reads", "Discarded Reads"]
    pconfig["use_legend"] = False
    pconfig["cpswitch"] = False

    self.add_section(
        name="Read Counts",
        anchor="barcode_correction_read_counts",
        description="",
        helptext="""
        This plot shows the total number of reads, broken down into valid reads (match perfectly with whitelist barcodes), barcode-corrected reads and discarded reads (too distant away from any whitelist barcodes to be corrected).
        This plot is generated based on the summary file from the correct_barcode module.
        """,
        plot=bargraph.plot(pdata, pcats, pconfig),
    )

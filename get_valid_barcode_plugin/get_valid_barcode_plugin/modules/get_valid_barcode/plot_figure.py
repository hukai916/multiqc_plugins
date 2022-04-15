import os

def plot_figure(self, dir_n, endswith = ".jpg", img_width = "32%", name = "To be added", description = "To be added", helptext = "To be added"):
    """
    Add a new section in the HTML report.
    Param: dir_n: .jpg file searching path folder (path must contain dir_n).
    Param: img_width: css style param (format: 32%).
    Param: name: name of the plot.
    Param: description: brief description of the plot.
    Param: helptext: help info for the plot.

    """

    plot = ""
    plot_path_all = ""
    for f in self.find_log_files('get_valid_barcode/jpeg'):
        if dir_n in f['root']:
            if f['fn'].endswith(endswith):
                plot_path = os.path.join(f['root'], f['fn'])
                self.get_valid_barcode[plot_path] = f
                plot_path_all = plot_path_all + plot_path + "<br>"
                plot = plot + "<figure style=\"border:solid 1px black; display:inline-block; width:" + img_width + "; margin:0.5%\">" + "<figcaption style=\"text-align: center; height: 40px; padding: 3px\">" + f['s_name'] + "</figcaption>" + " <img width=100% src=\"" + plot_path + "\">" + " </figure>"
    self.add_section(
            name = name,
            description = "<h4>" + description + "</h4><br>"+ "<b>Plot location:<br></b> " + plot_path_all,
            helptext = helptext,
            plot = plot
        )

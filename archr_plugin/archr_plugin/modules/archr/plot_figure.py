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
    for f in self.find_log_files('archr/jpeg'):
        if dir_n in f['root']:
            if f['fn'].endswith(endswith):
                plot_path = os.path.join(f['root'], f['fn'])
                self.archr[plot_path] = f
                plot_path_all = plot_path_all + plot_path + "<br>"
                plot = plot + "<figure style=\"border:solid 1px black; display:inline-block; width:" + img_width + "; margin:0.5%\">" + "<figcaption style=\"text-align: center; height: 40px; padding: 3px\">" + f['s_name'] + "</figcaption>" + " <img width=100% src=\"" + plot_path + "\">" + " </figure>"
    if plot == "":
        # deal with amulet filter module:
        if dir_n == "amulet_filter_doublets/":
            self.add_section(
                    name = name,
                    description = "<h4>" + description + "</h4><br>",
                    helptext = helptext,
                    plot = "<h3>Refer to ./amulet_doublets.txt for a list of detected doublets.</h3>"
                 )
        else:
            self.add_section(
                    name = name,
                    description = "<h4>" + description + "</h4><br>",
                    helptext = helptext,
                    # plot = "<h3>N/A</h3>"
                    plot = ""
                )
    else:
        self.add_section(
                name = name,
                description = "<h4>" + description + "</h4><br>"+ "<b>Plot location:<br></b> " + plot_path_all,
                helptext = helptext,
                plot = plot
            )

# Below are deprecated:
# for f in self.find_log_files('archr/jpeg'):
#     if "archr_create_arrowfiles" in f['root']:
#         if f['fn'].endswith("Fragment_Size_Distribution.jpg"):
#             plot_path = os.path.join(f['root'], f['fn'])
#             self.archr[plot_path] = f
#             self.add_section(
#                 name = "Arrowfile QC1: " + f['s_name'],
#                 description = '<h4>ArchR arrowfile fragment distribution for each sample.</h4><br>'+ "<b>Plot location:</b> " + plot_path,
#                 helptext = '''
#                 To be added.
#                 ''',
#                 plot = "<img width=\"700\" src=\"" + plot_path + "\">"
#             )

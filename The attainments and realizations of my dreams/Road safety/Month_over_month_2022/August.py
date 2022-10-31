import matplotlib.cm as cm
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.image as image

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

month = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug"]

deaths = [[13, 23, 29, 28, 24, 23],  # January
          [7, 16, 20, 24, 20, 30],   # February
          [9, 29, 14, 27, 34, 43],   # March
          [8, 25, 23, 23, 27, 31],   # April
          [7, 34, 16, 27, 27, 27],   # May
          [4, 25, 27, 15, 23, 26],   # June
          [4, 27, 16, 24, 28, 31],   # July
          [6, 26, 20, 31, 22, 33],   # August
          ]

df = pd.DataFrame(data=deaths,
                  index=month,
                  columns=administrative_duty)
print(df)

# Get some pastel shades for the colors[3]

# Matplotlib has a number of built-in colormaps accessible via matplotlib.cm.get_cmap.[4]
cmap = cm.get_cmap("YlOrRd")  # Colormap reference[5]
colors = cmap(np.linspace(0, 0.5, len(month)))
n_rows = len(deaths)

index = np.arange(len(administrative_duty)) + 0.3
bar_width = 0.4

figure, (axes, axes2) = plt.subplots(2, figsize=(9, 8))

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(administrative_duty))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plot = axes.bar(index, deaths[row], bar_width, bottom=y_offset, color=colors[row])
    #    axes.bar_label(axes.containers[0], label_type='center')
    y_offset = y_offset + deaths[row]
    cell_text.append([x for x in y_offset])

    i = 0

    # Each iteration of this for loop labels each bar with corresponding value for the given year
    for rectangle in plot:
        height = rectangle.get_height()
        axes.text(rectangle.get_x() + rectangle.get_width() / 2, y_offset[i], '%d' % int(y_offset[i]),
                  horizontalalignment='center', verticalalignment='bottom')

        i = i + 1

# Add a table at the bottom of the axes
the_table = axes.table(cellText=cell_text,
                       rowLabels=month,
                       rowColours=colors,
                       colLabels=administrative_duty,
                       loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

axes.set_ylabel("The number of deaths")
axes.set_xticks([])
axes.set_title("The Cumulative Number of Deaths in Road Accident\nin Taiwan by Region (2022/01-08)")

axes.grid(True)  # pyplot.grid [1][2]

# Count the grand total automatically
sum_TPE = deaths[0][0] + deaths[1][0] + deaths[2][0] + deaths[3][0] + deaths[4][0] + deaths[5][0] + deaths[6][0] + deaths[7][0]
sum_NTP = deaths[0][1] + deaths[1][1] + deaths[2][1] + deaths[3][1] + deaths[4][1] + deaths[5][1] + deaths[6][1] + deaths[7][1]
sum_TAO = deaths[0][2] + deaths[1][2] + deaths[2][2] + deaths[3][2] + deaths[4][2] + deaths[5][2] + deaths[6][2] + deaths[7][2]
sum_TCH = deaths[0][3] + deaths[1][3] + deaths[2][3] + deaths[3][3] + deaths[4][3] + deaths[5][3] + deaths[6][3] + deaths[7][3]
sum_TNA = deaths[0][4] + deaths[1][4] + deaths[2][4] + deaths[3][4] + deaths[4][4] + deaths[5][4] + deaths[6][4] + deaths[7][4]
sum_KAO = deaths[0][5] + deaths[1][5] + deaths[2][5] + deaths[3][5] + deaths[4][5] + deaths[5][5] + deaths[6][5] + deaths[7][5]


axes2.bar(administrative_duty, [sum_TPE, sum_NTP, sum_TAO, sum_TCH, sum_TNA, sum_KAO])
axes2.bar_label(axes2.containers[0], label_type='edge')
axes2.plot(administrative_duty, [sum_TPE, sum_NTP, sum_TAO, sum_TCH, sum_TNA, sum_KAO], '-o', color='orange')

figure.tight_layout()

# matplotlib text [1][2]
text = figure.text(0.5, 0.01,
                   'Reference:https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=100',
                   horizontalalignment='center',
                   verticalalignment='center',
                   size=12,
                   fontproperties='MS Gothic')

text.set_path_effects([path_effects.Normal()])

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=100, yo=700, alpha=0.9)

# Insert text watermark
plt.text(x=0.6, y=0.5, s="CC-BY 4.0", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation='20', transform=axes2.transAxes)

plt.show()

# References:
# 1. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
# 2. https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html#sphx-glr-gallery-subplots-axes-and-figures-geo-demo-py
# 3. https://stackoverflow.com/a/51454824
# 4. https://matplotlib.org/stable/tutorials/colors/colormaps.html
# 5. https://matplotlib.org/stable/gallery/color/colormap_reference.html

# Adapted from: https://matplotlib.org/stable/gallery/misc/table_demo.html

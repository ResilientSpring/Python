import matplotlib.cm as cm
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

month = ["Jan", "Feb"]

month_as_of_now = ["Jan", "Feb"]

deaths = [[13, 23, 29, 28, 24, 23],  # January
          [7, 16, 20, 24, 19, 30],  # February
          ]

df = pd.DataFrame(data=deaths,
                  index=month_as_of_now,
                  columns=administrative_duty)
print(df)

# Get some pastel shades for the colors[3]

# Matplotlib has a number of built-in colormaps accessible via matplotlib.cm.get_cmap.[4]
cmap = cm.get_cmap("YlOrRd")  # Colormap reference[5]
colors = cmap(np.linspace(0, 0.5, len(month_as_of_now)))
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
                       rowLabels=month_as_of_now,
                       rowColours=colors,
                       colLabels=administrative_duty,
                       loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

axes.set_ylabel("The number of deaths")
axes.set_xticks([])
axes.set_title("The Cumulative Number of Deaths in Road Accident\nin Taiwan by Region (2021/01-09)")

axes.grid(True)  # pyplot.grid [1][2]

axes2.bar(administrative_duty, [20, 39, 49, 52, 43, 53])
axes2.bar_label(axes2.containers[0], label_type='edge')
axes2.plot(administrative_duty, [20, 39, 49, 52, 43, 53], '-o', color='orange')

figure.tight_layout()

# matplotlib text [1][2]
text = figure.text(0.5, 0.01,
                   'Reference:https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=100',
                   horizontalalignment='center',
                   verticalalignment='center',
                   size=12,
                   fontproperties='MS Gothic')

text.set_path_effects([path_effects.Normal()])

plt.show()

# References:
# 1. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
# 2. https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html#sphx-glr-gallery-subplots-axes-and-figures-geo-demo-py
# 3. https://stackoverflow.com/a/51454824
# 4. https://matplotlib.org/stable/tutorials/colors/colormaps.html
# 5. https://matplotlib.org/stable/gallery/color/colormap_reference.html

# Adapted from: https://matplotlib.org/stable/gallery/misc/table_demo.html

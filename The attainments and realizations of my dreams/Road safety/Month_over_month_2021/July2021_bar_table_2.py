import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

month_as_of_now = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

deaths = [[14, 30, 18, 28, 31, 31], # Jan
          [23, 55, 38, 46, 62, 70], # Feb
          [36, 70, 56, 82, 83, 98], # Mar
          [47, 85, 77, 106, 106, 123], # Apr
          [57, 106, 99, 128, 147, 153], # May
          [66, 123, 123, 151, 172, 177], # Jun
          [73, 146, 145, 178, 190, 193], # Jul
          ]

df = pd.DataFrame(data=deaths,
                  index=month_as_of_now,
                  columns=administrative_duty)
print(df)

# Get some pastel shades for the colors
cmap = cm.get_cmap("Spectral") # [3]
colors = cmap(np.linspace(0, 0.5, len(month_as_of_now)))
n_rows = len(deaths)

index = np.arange(len(administrative_duty)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(administrative_duty))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, deaths[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + deaths[row]
    cell_text.append([x for x in y_offset])


# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=month_as_of_now,
                      rowColours=colors,
                      colLabels=administrative_duty,
                      loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("The number of deaths")
plt.xticks([])
plt.title("The Cumulative Number of Deaths in Road Accident\nin Taiwan by Region (2021/01-07)")

plt.grid(True) # pyplot.grid [1][2]

plt.tight_layout()

plt.show()

# References:
# 1. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
# 2. https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html#sphx-glr-gallery-subplots-axes-and-figures-geo-demo-py
# 3. https://stackoverflow.com/a/51454824

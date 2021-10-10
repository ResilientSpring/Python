import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# table's row
rows = ['2011', '2012', '2013', '2014', '2015']

# table's column
columns = ('7Ah', '35Ah', '40Ah', '135Ah', '150Ah', '150Ah')

# table's data
data = [[75, 144, 114, 102, 108],
        [90, 126, 102, 84, 126],
        [96, 114, 75, 105, 135],
        [105, 90, 150, 90, 75],
        [90, 75, 135, 75, 90]]

# Define the range and scale for the y axis.
values = np.arange(0, 600, 100)

cmap = cm.get_cmap("Spectral")
# Specify the color spectrum to be used.  Each year will be represented in a different color:
colors = cmap(np.linspace(0, 0.5, len(rows)))

# Define x axis ticks where the bars are to be plotted.
index = np.arange(len(columns)) + 0.3

# Initialize the vertical offset for the stacked bar chart
y_offset = np.zeros(len(columns))

# Specify the area for the plot in terms of figure and axes.
figure, axes = plt.subplots()

# Plot bars and create text labels for the table.

# Initialize the list where data for the table is save.
cell_text = []

n_rows = len(data)

# Each iteration of the for loop plots one year of data (for all battery ratings in one color).
for row in range(n_rows):
    plot = axes.bar(index, data[row], 0.5, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x) for x in y_offset])
    i = 0

    # Each iteration of this for loop labels each bar with corresponding value for the given year
    for rectangle in plot:
        height = rectangle.get_height()
        axes.text(rectangle.get_x() + rectangle.get_width() / 2, y_offset[i], '%d' % int(y_offset[i]),
                  horizontalalignment='center', verticalalignment='bottom')

        i = i + 1

# Add a table to the bottom of the axes
table = axes.table(cellText=cell_text,
                   rowLabels=rows,
                   rowColours=colors,
                   colLabels=columns,
                   loc='bottom')

axes.set_ylabel("Units Sold")
axes.set_xticks([])
axes.set_title("The Number Of Batteries Sold Per Year")

plt.show()

# Reference: https://airtw.epa.gov.tw/CHT/Query/Bad_Day.aspx
# Source: https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html#sphx-glr-gallery-lines-bars-and-markers-hat-graph-py
import numpy as np
import matplotlib.pyplot as plt


def hat_graph(ax, xlabels, values, group_labels):
    """
    Create a hat graph.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to plot into.
    xlabels : list of str
        The category names to be displayed on the x-axis.
    values : (M, N) array-like
        The data values.
        Rows are the groups (len(group_labels) == M).
        Columns are the categories (len(xlabels) == N).
    group_labels : list of str
        The group labels displayed in the legend.
    """

    def label_bars(heights, rects):
        """Attach a text label on top of each bar."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 points vertical offset.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # spacing between hat groups
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# initialise labels and a numpy array make sure you have
# N labels of N number of values in the array
xlabels = ['2018', '\'19', '\'20', '\'21', '\'22']
Taipei = np.array([3, 0, 1, 0, 0])              # Taipei + New Taipei
Kaohsiung = np.array([22, 8, 9, 15, 0])          # Kaohsiung

fig, ax = plt.subplots()
hat_graph(ax, xlabels, [Taipei, Kaohsiung], ['Taipei', 'Kaohsiung'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year\nReference: https://airtw.epa.gov.tw/CHT/Query/Bad_Day.aspx')
ax.set_ylabel('Days polluted by the unsafe levels of AQI')
ax.set_ylim(0, 31)
ax.set_title('The number of Days of December with Air Quality Index > 100')
ax.legend()

fig.tight_layout()
plt.show()
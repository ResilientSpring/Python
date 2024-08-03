import matplotlib.pyplot as plt
import numpy as np

Year = ("2022", "2023", "2024")
penguin_means = {
    'Taipei': (171.58, 177.48, 190.71),
    'New Taipei': (186.48, 197.57, 212.48),
    'Taoyuan': (141.05, ),
    'Taichung': (151.20, ),
    'Tainan': (102.06, ),
    'Kaohsiung': (151.44, 160.85, 169.57),
}

x = np.arange(len(Year))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('New Taiwan Dollar (billion)')
ax.set_title('Annual Expenditure by Local Government\n (Yearly distribution of taxpayer\'s money)')
ax.set_xticks(x + width, Year)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(80, 220)

plt.xlabel("Reference  https://www.dgbas.gov.tw/News.aspx?n=1525&sms=10694")

plt.show()

# References:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
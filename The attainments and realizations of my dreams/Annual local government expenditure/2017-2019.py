import matplotlib.pyplot as plt
import numpy as np

Year = ("2017", "2018", "2019")
penguin_means = {
    'Taipei': (165.75, 172.55, 164.91),
    'New Taipei': (156.31, 162.03, 163.66),
    'Taoyuan': (102.23, 110.05, 114.51),
    'Taichung': (126.77, 129.68, 124.65),
    'Tainan': (79.84, 84.85, 86.25),
    'Kaohsiung': (128.79, 129.16, 133.48),
}

x = np.arange(len(Year))  # the label locations
width = 0.10  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='tight', figsize=(15, 7)) # [1]

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
ax.set_ylim(80, 180)

plt.xlabel("Reference  https://www.dgbas.gov.tw/News.aspx?n=1525&sms=10694")

plt.show()

# References:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
# 1. https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide

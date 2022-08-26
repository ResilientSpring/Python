import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()

fig, ax = plt.subplots(figsize=(8, 8))

city = ('Taipei', 'New Taipei', 'Taoyuan', 'Taichung', 'Tainan', 'Kaohsiung')
y_pos = np.arange(len(city))
births = [8297, 12111, 10216, 9955, 5078, 9013]
error = np.random.rand(len(city))

horizontal_bar = ax.barh(y_pos, births, xerr=error, align='center')
ax.set_yticks(y_pos, labels=city)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("# of births\nReference: https://statis.moi.gov.tw/micst/stmain.jsp?sys=100")
ax.set_title('The number of births by city (2022/01-07) ')

# Label with given captions, custom padding and annotate options
ax.bar_label(horizontal_bar, labels=births, padding=8, color='b', fontsize=14)

plt.show()

# References:
# 1. https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html

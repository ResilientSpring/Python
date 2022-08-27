import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as image

plt.rcdefaults()

fig, ax = plt.subplots(figsize=(7, 7))

city = ('Taipei', 'New Taipei', 'Taoyuan', 'Taichung', 'Tainan', 'Kaohsiung')
y_pos = np.arange(len(city))
births = [25042, 31611, 23356, 24338, 13773, 20260]
error = np.random.rand(len(city))

horizontal_bar = ax.barh(y_pos, births, xerr=error, align='center')
ax.set_yticks(y_pos, labels=city)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("# of births\nReference: https://statis.moi.gov.tw/micst/stmain.jsp?sys=100")
ax.set_title('The number of births in Taiwan by city (2017)')

# Label with given captions, custom padding and annotate options
ax.bar_label(horizontal_bar, labels=births, padding=8, color='b', fontsize=14)

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=600, yo=650, alpha=0.9)

plt.show()

# References:
# 1. https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html

# Data: https://statis.moi.gov.tw/micst/stmain.jsp?sys=220&ym=10600&ymt=10600&kind=21&type=1&funid=c0120101&cycle=41&outmode=0&compmode=0&outkind=1&fld0=1&codspc0=0,2,3,2,6,1,9,1,12,1,15,14,&rdm=immoqeji

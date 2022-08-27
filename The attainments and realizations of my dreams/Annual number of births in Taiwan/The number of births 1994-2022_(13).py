import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.colors as colour
import matplotlib.image as image

# Using the magic encoding
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic")

year_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
               24, 25, 26, 27, 28, 29]

number_of_births = [322938, 329581, 325545, 326002, 271450, 283661, 305312, 260354, 247530, 227070,
                    216419, 205854, 204459, 204414, 198733, 191310, 166886, 196627, 229481, 199113,
                    210383, 213598, 208440, 193844, 181601, 177767, 165249, 153820,
                    (13137 + 9617 + 12788 + 11222 + 9442 + 10943 + 10950)]

label_year_text = ["1994", "'95", "'96", "'97", "'98", "'99", "2000", "'01", "'02", "'03", "'04", "'05",
                   "'06", "'07", "'08", "'09", "'10", "'11", "'12", "'13", "'14", "'15", "'16", "'17",
                   "'18", "'19", "'20", "'21", "'22"]

fig, axe = plt.subplots(nrows=1, ncols=1, figsize=(24, 13))
axe.set_xticks(year_number, labels=label_year_text, rotation=7, fontsize=12)
axe.tick_params(axis='y', labelsize=12)

plot = axe.bar(year_number, number_of_births, align='center', width=0.3, color=colour.CSS4_COLORS.get('pink'))

for rect in plot:
    height = rect.get_height()
    axe.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
             '%d' % int(height), ha='center', va='bottom', fontsize=12, rotation=4)

axe.set_title(label="1994-2022/07 台灣年度出生人數\n Annual number of births in Taiwan", fontsize=20)

axe.set_ylabel("The number of births")
axe.set_xlabel("Year")

axe.set_ylim(78000, 330000)

plt.margins(x=0, y=0, tight=False)  # [1][2]
fig.tight_layout()  # [3]

text = fig.text(0.5, 0.7,
                'Reference:https://statis.moi.gov.tw/micst/stmain.jsp?sys=100',
                horizontalalignment='center',
                verticalalignment='center',
                size=13,
                fontproperties='MS Gothic')


img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=2000, yo=850, alpha=0.9)

plt.show()

# References:
# 1. https://www.google.com/search?q=matplotlib+margins
# 2. https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/axes_margins.html
# 3. https://stackoverflow.com/a/4046233

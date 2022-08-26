import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
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

fig, axe = plt.subplots(nrows=1, ncols=1, figsize=(8, 7))
axe.set_xticks(year_number, labels=label_year_text, rotation=7, fontsize=12)
axe.tick_params(axis='y', labelsize=12)

plot = axe.bar(year_number, number_of_births)

for rect in plot:
    height = rect.get_height()
    axe.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)


axe.set_title(label="1994-2022/07 台灣年度出生人數\n Annual number of births in Taiwan", fontsize=20)

# axe.set_ylabel("The number of births")
axe.set_xlabel("Year")

axe.set_ylim(150000, 330000)

plt.show()

# References:
# 1. https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html
# 2. https://numpy.org/doc/stable/reference/generated/numpy.arange.html

# Data: https://statis.moi.gov.tw/micst/stmain.jsp?sys=220&ym=8300&ymt=11000&kind=21&type=1&funid=c0120101&cycle=4&outmode=0&compmode=0&outkind=1&fld0=1&cod00=1&rdm=fu0Necq9

import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib
import numpy as np
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic")

Year = ("2022", "2023", "2024")
penguin_means = {
                     # Taipei + New Taipei + Keelung
    'Greater Taipei': (171.58+186.48+21.15, 177.48+197.57+19.63, 190.71+212.48+24.09),
                     # Taoyuan + Hsinchu county + Hsinchu city + Miaoli
    'Taoyuan-Hsinchu_Miaoli': (141.05+32.36+25.61+21.56,
                               142.99+34.82+25.51+22.98,
                               156.80+35.43+28.11+25.05),

    'Taichung-Changhua-Nantou': (151.20+56.60+28.90, 150.48+58.89+24.92, 177.22+64.45+33.72),

                     # Yunlin + Chiayi county + Chiayi city + Tainan
    'Yunlin-Chiayi-Tainan': (37.30+28.35+16.62+102.06,
                             36.30+27.41+18.38+102.56,
                             40.43+33.22+19.35+116.94),

    'Kaohsiung-Pingtung': (151.44+47.11, 160.85+50.33, 169.57+55.85),
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
ax.set_title('Annual Expenditure by Local Governments\n (Yearly distribution of taxpayer\'s money at metro level)')
ax.set_xticks(x + width, Year)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(150, 450)

plt.xlabel("Reference  https://www.dgbas.gov.tw/News.aspx?n=1525&sms=10694")

img = image.imread('CC0.png')

plt.figimage(X=img, xo=1050, yo=650, alpha=0.9)

# Insert text watermark
plt.text(x=0.25, y=0.65, s="CC0 No Copyright\n無版權圖片", fontsize=30, color='grey', alpha=0.9,
         ha='center', va='center', rotation=30, #rotation='30',
         transform=ax.transAxes)

plt.show()

# References:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
# 1. https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide

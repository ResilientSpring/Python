import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.cbook as cbook
import matplotlib.colors as colour
import matplotlib.image as image
# Using the magic encoding
# -*- coding: utf-8 -*-
from matplotlib.transforms import IdentityTransform

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5, 6]
position_vacancies = [107229, 59148, 43509, 54374, 24843, 34872]

label = ["台北市\nTaipei", "新北市\nNew Taipei", "桃園\nTaoyuan", "台中\nTaichung", "台南\nTainan", "高雄\n Kaohsiung"]

fig, ax = plt.subplots(figsize=(9, 9), facecolor=(.18, .31, .31)) # [1]
ax.set_facecolor('#eafff5')  # [1]

plt.xticks(region_num, labels=label, rotation=7, fontsize=12)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12)

plot = ax.bar(region_num, position_vacancies, edgecolor='cyan', color=[colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('palegreen'),
                                                                       colour.CSS4_COLORS.get('palegreen')])

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

plt.title("2023/01 台灣各城市職缺數\n the number of job openings in Taiwan by city", fontsize=20)

# plt.ylabel("")
plt.xlabel("參考資料 Reference: https://web.archive.org/web/20230121040108/https://www.104.com.tw/jobs/main/category/?jobsource=category")

plt.ylim(24500, 100000)

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=800, yo=800, alpha=0.9)

# Insert text watermark [1]
plt.text(x=0.6, y=0.7, s="CC-BY 4.0", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation=30,
         transform=ax.transAxes)


plt.show()

# Reference:
# 1. https://matplotlib.org/stable/gallery/color/color_demo.html#sphx-glr-gallery-color-color-demo-py

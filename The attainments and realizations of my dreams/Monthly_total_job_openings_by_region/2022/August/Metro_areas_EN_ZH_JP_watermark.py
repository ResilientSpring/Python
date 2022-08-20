import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cbook as cbook
import matplotlib.image as image
# Using the magic encoding
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5]
position_vacancies = [180741, 89132, 74250, 38822, 41763]

label = ["大台北 Greater\nTaipei", "桃園 Taoyuan\n新竹 Hsinchu\n苗栗 Miaoli", "台中 Taichung\n彰化 Changhua\n南投 Nantou",
         "雲林 Yunlin\n嘉義 Chiayi\n台南 Tainan", "高雄 Kaohsiung\n屏東 Pingtung"]

fig, ax = plt.subplots(figsize=(9, 9))
plt.xticks(region_num, labels=label, rotation=7, fontsize=12)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12) # [2]

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

plt.title("2022/08 台灣各生活圈職缺數\n the number of job openings in Taiwan by metro", fontsize=20)

# plt.ylabel("")
plt.xlabel("參考資料 Reference: https://web.archive.org/web/20220820070855/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(38000, 165000)

img = image.imread('CC-BY.png') # Load image. [1]

plt.figimage(X=img, xo=20, yo=20, alpha=0.5)  # Insert watermark image. [2]

plt.show()

# Reference:
# 1. https://matplotlib.org/stable/tutorials/introductory/images.html
# 2. https://matplotlib.org/stable/gallery/images_contours_and_fields/watermark_image.html
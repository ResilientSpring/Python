import matplotlib.pyplot as plt
import matplotlib
import matplotlib.image as image

# Using the magic encoding
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5]
position_vacancies = [140966, 72721, 61138, 31208, 31440]

label = ["大台北 Greater\nTaipei", "桃園 Taoyuan\n新竹 Hsinchu\n苗栗 Miaoli", "台中 Taichung\n彰化 Changhua\n南投 Nantou",
         "雲林 Yunlin\n嘉義 Chiayi\n台南 Tainan", "高雄 Kaohsiung\n屏東 Pingtung"]

fig, ax = plt.subplots(figsize=(9, 9))
plt.xticks(region_num, labels=label, rotation=7, fontsize=12) # [1]
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12) # [2]

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12) # [1]

plt.title("2021/09 台灣各生活圈職缺數\n the number of job openings in Taiwan by metro", fontsize=20) # [1]

# plt.ylabel("")
plt.xlabel("參考資料 Reference: https://web.archive.org/web/20210927094609/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(30000, 130000)

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=800, yo=800, alpha=0.9)

plt.text(x=0.6, y=0.7, s="CC-BY 4.0", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation='30',
         transform=ax.transAxes)

plt.show()

# Reference:
# 1. https://stackoverflow.com/a/12444777/
# 2. https://stackoverflow.com/a/11386056/
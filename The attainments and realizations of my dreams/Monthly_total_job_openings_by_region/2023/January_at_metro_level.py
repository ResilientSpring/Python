import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cbook as cbook
import matplotlib.colors as colour
import matplotlib.image as image
# Using the magic encoding
# -*- coding: utf-8 -*-
from matplotlib.transforms import IdentityTransform

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5]
position_vacancies = [1956+107229+59148+4074, 43509+31609+6060, 54374+3290+9152, 4148+6256+24843, 34872+4328]

label = ["大台北 Greater\nTaipei", "桃園 Taoyuan\n新竹 Hsinchu\n苗栗 Miaoli", "台中 Taichung\n彰化 Changhua\n南投 Nantou",
         "雲林 Yunlin\n嘉義 Chiayi\n台南 Tainan", "高雄 Kaohsiung\n屏東 Pingtung"]

fig, ax = plt.subplots(figsize=(9, 9))
plt.xticks(region_num, labels=label, rotation=7, fontsize=12)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12) # [2]

plot = ax.bar(region_num, position_vacancies, edgecolor='cyan', color=[colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('deepskyblue'),
                                                                       colour.CSS4_COLORS.get('palegreen'),
                                                                       colour.CSS4_COLORS.get('palegreen')]) #[4][5][6]

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

plt.title("2023/01 台灣各生活圈職缺數\n the number of job openings in Taiwan by metro", fontsize=20)

# plt.ylabel("")
plt.xlabel("參考資料 https://web.archive.org/web/20230121040108/https://www.104.com.tw/jobs/main/category/?jobsource=category")

plt.ylim(36500, 160000)

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=800, yo=800, alpha=0.9)

# Insert text watermark [1]
plt.text(x=0.6, y=0.7, s="CC-BY 4.0", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation=30,
         transform=ax.transAxes) # data coordinates [2] [Note1] [3] [Note2]

plt.show()

# Reference:
# 1. https://matplotlib.org/stable/gallery/text_labels_and_annotations/watermark_text.html
# 2. https://matplotlib.org/stable/tutorials/advanced/transforms_tutorial.html
# 3. https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text
# 4. https://www.google.com/search?q=matplotlib+bar+color
# 5. https://www.python-graph-gallery.com/3-control-color-of-barplots
# 6. https://matplotlib.org/stable/gallery/color/named_colors.html

# Notes:
# 1. pixel coordinate system of the display window; (0, 0) is bottom left of the window,
# and (width, height) is top right of the display window in pixels.[2]
#
# 2. default transform specifies that text is in data coords,
# alternatively, you can specify text in axis coords ((0, 0) is lower-left and (1, 1) is upper-right).
# The example below places text in the center of the Axes:[3]

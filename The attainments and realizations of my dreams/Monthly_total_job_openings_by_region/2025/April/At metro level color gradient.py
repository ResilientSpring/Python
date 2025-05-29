import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cbook as cbook
import matplotlib.colors as colour
import numpy as np
import matplotlib.image as image
# Using the magic encoding
# -*- coding: utf-8 -*-
from matplotlib.transforms import IdentityTransform

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5]
position_vacancies = [2660+128675+78967+4367, 54586+36351+7237, 67632+12384+3872, 5138+7802+31252, 43547+5087]

label = ["大台北 Greater\nTaipei", "桃園 Taoyuan\n新竹 Hsinchu\n苗栗 Miaoli", "台中 Taichung\n彰化 Changhua\n南投 Nantou",
         "雲林 Yunlin\n嘉義 Chiayi\n台南 Tainan", "高雄 Kaohsiung\n屏東 Pingtung"]

fig, ax = plt.subplots(figsize=(9, 9))
plt.xticks(region_num, labels=label, rotation=7, fontsize=12)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12) # [2]

plot = ax.bar(region_num, position_vacancies, edgecolor='black', color=[colour.CSS4_COLORS.get('darkblue'),
                                                                        colour.CSS4_COLORS.get('mediumblue'),
                                                                        colour.CSS4_COLORS.get('blue'),
                                                                        'none',
                                                                        colour.CSS4_COLORS.get('palegreen')]) #[4][5][6]

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

plt.title("2025/04 台灣各生活圈職缺數\n the number of job openings in Taiwan by metro", fontsize=20)

# plt.ylabel("")
plt.xlabel("參考資料 Reference  https://archive.ph/WHbv4")

plt.ylim(40000, 200000)

img = image.imread('CC0.png')  # CC0.png downloaded from [7].

plt.figimage(X=img, xo=800, yo=800, alpha=0.9)

# Insert text watermark [1]
plt.text(x=0.6, y=0.7, s="Non-copyrighted image\n無版權圖片", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation=30,
         transform=ax.transAxes) # data coordinates [2] [Note1] [3] [Note2]

cmap = matplotlib.colormaps.get_cmap('winter')  # [8][9]

counter = 0

for rect in plot: # [8][9]

    if rect is not None:

        counter = counter + 1

        if counter == 4:

            # Bar position and size
            x = rect.get_x()
            width = rect.get_width()
            height = rect.get_height()

            # Create a grid inside the bar
            nx = 100  # Number of divisions horizontally
            ny = 100  # Number of divisions vertically
            X = np.linspace(x, x + width, nx)
            Y = np.linspace(0, height, ny)
            X, Y = np.meshgrid(X, Y)

            # Color based on horizontal position (left to right)
            Z = (X - x) / width  # Normalize X inside the bar (0 to 1)

            # Draw gradient
            ax.pcolormesh(X, Y, Z, cmap=cmap, shading='auto')




plt.show()

# Reference:
# 1. https://matplotlib.org/stable/gallery/text_labels_and_annotations/watermark_text.html
# 2. https://matplotlib.org/stable/tutorials/advanced/transforms_tutorial.html
# 3. https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text
# 4. https://www.google.com/search?q=matplotlib+bar+color
# 5. https://www.python-graph-gallery.com/3-control-color-of-barplots
# 6. https://matplotlib.org/stable/gallery/color/named_colors.html
# 7. https://creativecommons.org/public-domain/cc0/
# 8. https://chatgpt.com/c/680c6f49-95b4-8008-85f4-3941744f62e4
# 9. Untitled5.ipynb @ my Google Colab.

# Notes:
# 1. pixel coordinate system of the display window; (0, 0) is bottom left of the window,
# and (width, height) is top right of the display window in pixels.[2]
#
# 2. default transform specifies that text is in data coords,
# alternatively, you can specify text in axis coords ((0, 0) is lower-left and (1, 1) is upper-right).
# The example below places text in the center of the Axes:[3]

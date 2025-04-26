import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cbook as cbook
import matplotlib.colors as colour
import matplotlib.image as image
# Using the magic encoding
# -*- coding: utf-8 -*-
from matplotlib.transforms import IdentityTransform

matplotlib.rc('font', family="MS Gothic")

region_num = [1]
position_vacancies = [39865]

label = ["高雄市\nKaohsiung City"]

fig, ax = plt.subplots(figsize=(9, 9))
plt.xticks(region_num, labels=label, rotation=7, fontsize=12)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12) # [2]

plot = ax.bar(region_num, position_vacancies, edgecolor='black', color=[colour.CSS4_COLORS.get('mediumslateblue')]) #[4][5][6]

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

plt.title("2024/02 台灣南北二城市職缺數\n the number of job openings in Taipei & Kaohsiung of Taiwan", fontsize=20)

# plt.ylabel("")
plt.xlabel("參考資料 Reference https://archive.ph/LPccQ")

plt.ylim(30000, 130000)

plt.show()

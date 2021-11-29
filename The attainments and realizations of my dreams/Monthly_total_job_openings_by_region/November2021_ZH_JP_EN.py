import matplotlib
import matplotlib.pyplot as plt
# Using the magic encoding
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic") # [1]

region_num = [1, 2, 3, 4, 5, 6, 7]
position_vacancies = [92415, 53496, 39357, 31572, 51570, 23956, 29969]

label = ["Taipei\n台北", "New Taipei\n新北", "Taoyuan\n桃園", "Hsinch\n新竹", "Taichung\n台中", "Tainan\n台南", "Kaohsiung\n高雄"]

fig, ax = plt.subplots(figsize=(8, 7))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2021/11 台灣各地區職缺數統計\nthe number of job openings in Taiwan by region", fontproperties="MS Gothic")

# plt.ylabel("")
plt.xlabel("Source&参照&出典: https://web.archive.org/web/20211128163303/https://www.104.com.tw/jb/category/?cat=2") # [2][3]

plt.ylim(20000, 90000)

plt.show()

# Reference:
# 1. https://stackoverflow.com/questions/10960463/non-ascii-characters-in-matplotlib
# 2. Google Translate
# 3. https://ja.wikipedia.org/wiki/高雄市#出典

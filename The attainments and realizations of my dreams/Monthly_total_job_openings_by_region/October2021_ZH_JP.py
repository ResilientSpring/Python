import matplotlib
import matplotlib.pyplot as plt

# Using the magic encoding
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5, 6, 7]
position_vacancies = [89351, 52065, 38298, 30692, 50527, 23497, 28960]

label = ["台北", "新北", "桃園", "新竹", "台中", "台南", "高雄"]

fig, ax = plt.subplots(figsize=(8, 7))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2021/10 台灣各地區職缺數統計\nthe number of job openings in Taiwan by region")

# plt.ylabel("")
plt.xlabel("Reference: https://web.archive.org/web/20211023110903/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(20000, 90000)

plt.show()

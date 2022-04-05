import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5, 6]
position_vacancies = [109262, 63982, 46161, 61036, 28391, 35120]

label = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

fig, ax = plt.subplots(figsize=(8, 7))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2022/03 the number of job openings in Taiwan by region")

# plt.ylabel("")
plt.xlabel("Reference: https://web.archive.org/web/20220130184455/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(20000, 100000)

plt.show()

import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5, 6, 7]
position_vacancies = [89351, 52065, 38298, 30692, 50527, 23497, 28960]

label = ["Taipei", "New Taipei", "Taoyuan", "Hsinchu", "Taichung", "Tainan", "Kaohsiung"]

fig, ax = plt.subplots(figsize=(8, 7))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2021/10 the number of job openings in Taiwan by region")

# plt.ylabel("")
plt.xlabel("https://web.archive.org/web/20211023110903/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(20000, 90000)

plt.show()

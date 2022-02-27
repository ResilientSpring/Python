import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5, 6, 7]
position_vacancies = [105740, 61783, 44534, 35054, 59418, 27771, 34083]

label = ["Taipei", "New Taipei", "Taoyuan", "Hsinchu", "Taichung", "Tainan", "Kaohsiung"]

fig, ax = plt.subplots(figsize=(8, 7))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2022/02 the number of job openings in Taiwan by region")

# plt.ylabel("")
plt.xlabel("Reference: https://web.archive.org/web/20220226163214/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(27500, 107000)

plt.show()

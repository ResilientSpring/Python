import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
position_vacancies = [85928, 50512, 37109, 29894, 5718, 48837, 9500,
                      3477, 4956, 22775, 27978, 3462]

label = ["Taipei", "New Taipei", "Taoyuan", "Hsinchu", "Miaoli", "Taichung", "Changhua",
         "Yunlin", "Chiayi", "Tainan", "Kaohsiung", "Pingtung"]

fig, ax = plt.subplots(figsize=(10, 9))  # [1]
plt.xticks(region_num, labels=label, rotation=47)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2021/09 the number of job openings in Taiwan by region")

# plt.ylabel("")
plt.xlabel("Reference: https://web.archive.org/web/20210927094609/https://www.104.com.tw/jb/category/?cat=2")

# plt.ylim(280, 560)

plt.show()

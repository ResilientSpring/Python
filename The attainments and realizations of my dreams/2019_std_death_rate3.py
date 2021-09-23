import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
death_rate = [289.6, 358.6, 361.5, 378.8, 387.4, 393.7, 402.4, 402.5, 406.4, 408.1,
              412.4, 413.1, 427.6, 437.3, 438.5, 439.3, 455.7, 493.5, 506.8, 545.2]

label = ["Taipei", "Hsinchu City", "New Taipei", "Taoyuan", "Taichung", "Hsinchu",
         "Penghu", "Changhua", "Chiayi City", "Yilan", "Keelung", "Tainan", "Kaohsiung",
         "Chiayi", "Miaoli", "Nantou", "Yunlin", "Hualien", "Pingtung", "Taitung"]

fig, ax = plt.subplots(figsize=(10, 8)) # [1]
plt.xticks(region_num, labels=label, rotation=47)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, death_rate)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002*height,
            '%d'%int(height), ha='center', va='bottom')

plt.title("2019 Standardized Death Rate By Region In Taiwan")

plt.ylabel("Death per 10 thousands people")
plt.xlabel("Reference: https://www.moi.gov.tw/cl.aspx?n=14661")

plt.ylim(280, 580)

plt.show()

# Reference:
# 1. https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
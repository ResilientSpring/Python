import matplotlib.pyplot as plt
import matplotlib.colors as colour

region_num = [1, 2]
position_vacancies = [120654, 39865]

label = ["Taipei City",
         "Kaohsiung City"]

fig, ax = plt.subplots(figsize=(9, 9))
plt.xticks(region_num, labels=label, rotation=0, fontsize=12)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])
plt.tick_params(axis='y', labelsize=12) # [2]

plot = ax.bar(region_num, position_vacancies, edgecolor='black', color=[colour.CSS4_COLORS.get('mediumslateblue'),
                                                                        colour.CSS4_COLORS.get('slateblue'),]) #[4][5][6]

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

plt.title("2024/02 the number of job openings in Taipei & Kaohsiung of Taiwan", fontsize=20)

# plt.ylabel("")
plt.xlabel("Reference https://archive.ph/LPccQ")

plt.ylim(30000, 130000)

plt.show()


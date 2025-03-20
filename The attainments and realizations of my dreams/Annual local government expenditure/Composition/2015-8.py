import matplotlib.pyplot as plt
import numpy as np

species = ('Taipei', 'New Taipei', "Taoyuan", 'Taichung', "Tainan", 'Kaohsiung')
allotted_money = {
    'Statutory': [34.95, 26.52, 17.12, 20.63, 17.44, 26.47],  #[1]:18
    'Federal discretionary subsidy': [17.12, 31.11, 15.21, 24.88, 22.85, 27.83], #[1]:25
}

sum = [allotted_money['Statutory'][0] + allotted_money["Federal discretionary subsidy"][0],
       allotted_money["Statutory"][1] + allotted_money["Federal discretionary subsidy"][1],
       allotted_money["Statutory"][2] + allotted_money["Federal discretionary subsidy"][2],
       allotted_money["Statutory"][3] + allotted_money["Federal discretionary subsidy"][3],
       allotted_money["Statutory"][4] + allotted_money["Federal discretionary subsidy"][4],
       allotted_money["Statutory"][5] + allotted_money["Federal discretionary subsidy"][5]
       ]

fig, ax = plt.subplots(figsize=(6, 9))
bottom = np.zeros(6)

p = 0

for sex, sex_count in allotted_money.items():
    p = ax.bar(species, sex_count, width=0.6, label=sex, bottom=bottom)  #[Note1]
    bottom += sex_count

    ax.bar_label(p, label_type='center')

    # for rect in p:
    #     height = rect.get_height()
    #     ax.text(rect.get_x() + rect.get_width() / 2., 2.001 * height,
    #             '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.bar_label(p, labels=[f'{s:.2f}' for s in sum], label_type="edge")  #[3]

# plot = ax.bar(region_num, position_vacancies, width=0.6)
#
# for rect in plot:
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
#             '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.set_title("2015's composition of local government's income \n (Unit: billion)")
ax.legend()

plt.show()

# References:
# 1. https://ws.dgbas.gov.tw/public/attachment/5611134736t64w6mty.pdf
# 2. https://matplotlib.org/3.8.4/api/_as_gen/matplotlib.axes.Axes.bar_label.html
# 3. https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html

# Notes:
# 1. when having duplicate values in categorical x data,
# these values map to the same numerical x coordinate, and hence the corresponding bars
# are drawn on top of each other. [2]

import matplotlib.pyplot as plt
import numpy as np

species = ('Taipei', 'New Taipei', "Taoyuan", 'Taichung', "Tainan", 'Kaohsiung')
sex_counts = {
    'Statutory': [34.95, 26.52, 17.12, 20.63, 17.44, 26.47],  #[1]:18
    'Federal discretionary subsidy': [17.12, 31.11, 15.21, 24.88, 22.85, 27.83], #[1]:25
}

position_vacancies = [sex_counts['Statutory'][0] + sex_counts["Federal discretionary subsidy"][0],
                      sex_counts["Statutory"][1] + sex_counts["Federal discretionary subsidy"][1],
                      sex_counts["Statutory"][2] + sex_counts["Federal discretionary subsidy"][2],
                      sex_counts["Statutory"][3] + sex_counts["Federal discretionary subsidy"][3],
                      sex_counts["Statutory"][4] + sex_counts["Federal discretionary subsidy"][4],
                      sex_counts["Statutory"][5] + sex_counts["Federal discretionary subsidy"][5]
                      ]

fig, ax = plt.subplots()
bottom = np.zeros(6)

p = 0

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width=0.6, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

    # for rect in p:
    #     height = rect.get_height()
    #     ax.text(rect.get_x() + rect.get_width() / 2., 2.001 * height,
    #             '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.bar_label(p, labels=position_vacancies, label_type="edge", fmt="%.2f")

# plot = ax.bar(region_num, position_vacancies, width=0.6)
#
# for rect in plot:
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
#             '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.set_title("2015's composition of local government's income")
ax.legend()

plt.show()

# References:
# 1. https://ws.dgbas.gov.tw/public/attachment/5611134736t64w6mty.pdf

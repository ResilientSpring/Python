import matplotlib.pyplot as plt
import numpy as np

species = ('Taipei', 'Taichung', 'Kaohsiung')
sex_counts = {
    'Statutory': np.array([73, 34, 61]),
    'Federal discretionary subsidy': np.array([71, 39, 58]),
}

region_num = [1, 2, 3]
position_vacancies = [sex_counts['Statutory'][0] + sex_counts["Federal discretionary subsidy"][0],
                      sex_counts["Statutory"][1] + sex_counts["Federal discretionary subsidy"][1],
                      sex_counts["Statutory"][2] + sex_counts["Federal discretionary subsidy"][2]]

fig, ax = plt.subplots()
bottom = np.zeros(3)

p = 0

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width=0.6, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

    # for rect in p:
    #     height = rect.get_height()
    #     ax.text(rect.get_x() + rect.get_width() / 2., 2.001 * height,
    #             '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.bar_label(p, labels=position_vacancies, label_type="edge")

# plot = ax.bar(region_num, position_vacancies, width=0.6)
#
# for rect in plot:
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
#             '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()

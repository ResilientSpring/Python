import matplotlib.pyplot as plt
import numpy as np

region_num = [1, 2, 3]
position_vacancies = [128075, 78000, 53560, 67473, 30503, 43279]

species = ('Taipei', 'Chinstrap', 'Kaohsiung')
sex_counts = {
    'Statutory': np.array([73, 34, 61]),
    'Basic subsidy': np.array([73, 34, 58]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')


plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom', fontsize=12)

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()

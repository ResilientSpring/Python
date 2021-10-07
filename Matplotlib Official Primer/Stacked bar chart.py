import matplotlib.pyplot as plt


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

#  the parameters yerr used for error bars,
ax.bar(labels, men_means, width, yerr=men_std, label='Men')

# and bottom to stack the women's bars on top of the men's bars.
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()

# Source: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html?highlight=stack

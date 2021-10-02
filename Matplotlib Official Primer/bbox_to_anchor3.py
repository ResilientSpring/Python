import pandas as pd
import matplotlib.pyplot as plt

data = {'var': ['TR', 'AC', 'F&B'], '2019 1Q': [6600, 1256, 588], '2019 2Q': [6566, 1309, 586], '2019 3Q': [7383, 1525, 673]}
df = pd.DataFrame(data)
df.set_index('var', inplace=True)

ax = df.T.plot.bar(stacked=True, figsize=(10, 5), rot=0)

for c in ax.containers:
    ax.bar_label(c, label_type='center')

ax.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()

# Source: https://stackoverflow.com/a/63856446/14900011

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create sample data as shown in the OP
np.random.seed(365)

people = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
bottomdata = 3 + 10 * np.random.rand(len(people))
topdata = 3 + 10 * np.random.rand(len(people))

# create the dataframe
df = pd.DataFrame({'Female': bottomdata, 'Male': topdata}, index=people)

print(df)

cm = 1 / 2.54

ax = df.plot(kind='bar', stacked=True, figsize=(28 * cm, 15 * cm))

for c in ax.containers:

    # customize the label to account for cases when there might not be a bar section

    labels = []
    for v in c:
        w = v.get_width()
        if w > 0:
            labels.append(f'{w:.2f}%')
        else:
            labels.append('')

    #   labels = [f'{w:.2f}%' if (w := v.get_width()) > 0 else '' for v in c ]

    # set the bar label
    ax.bar_label(c, labels=labels, label_type='center')

    # uncomment and use the next line if there are no nan or 0 length sections; just use fmt to add a % (the previous two lines of code are not needed, in this case)
#     ax.bar_label(c, fmt='%.2f%%', label_type='center')

# move the legend
ax.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0.)

# add labels
ax.set_ylabel("People", fontsize=18)
ax.set_xlabel("Percent", fontsize=18)
plt.show()

# Source: https://stackoverflow.com/a/64202669/14900011

# References:
# 1. https://www.google.com/search?q=python+3.8+vs+3.7
# 2. https://docs.python.org/3/whatsnew/3.8.html
# 3. https://www.google.com/search?q=walrus+operator
# 4. https://towardsdatascience.com/the-walrus-operator-7971cd339d7d
# 5. https://www.geeksforgeeks.org/display-percentage-above-bar-chart-in-matplotlib/

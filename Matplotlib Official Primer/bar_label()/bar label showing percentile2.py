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

ax = df.plot(kind='barh', stacked=True, figsize=(8, 6))

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

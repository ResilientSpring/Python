import numpy as np
import matplotlib.pyplot as plt

x = [u'INFO', u'CUISINE', u'TYPE_OF_PLACE', u'DRINK', u'PLACE', u'MEAL_TIME', u'DISH', u'NEIGHBOURHOOD']
y = [160, 167, 137, 18, 120, 36, 155, 130]
ind = np.arange(len(y))

fig, ax = plt.subplots()
ax.barh(ind, y)
ax.set_yticks(ind)
ax.set_yticklabels(x)

# new helper method to auto-label bars
ax.bar_label(ax.containers[0])

plt.show()

# Source: https://stackoverflow.com/a/68107816/14900011

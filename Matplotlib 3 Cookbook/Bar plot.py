import matplotlib.pyplot as plt
import numpy as np
import calendar

month_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

units_sold = [500, 600, 750, 900, 1100, 1050, 1000, 950, 800, 700, 550, 450]

fig, ax = plt.subplots()

plt.xticks(month_num, calendar.month_name[1:13], rotation=27)

plot = ax.bar(month_num, units_sold)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002*height,
            '%d'%int(height), ha='center', va='bottom')

plt.show()

import matplotlib.pyplot as plt
import calendar

# matplotlib accepts only floating point data types as its arguments for data.
# So months have to be represented in numerical format.
month_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
units_sold = [500, 600, 750, 900, 1100, 1050, 1000, 950, 800, 700, 550, 450]

fig, ax = plt.subplots()

# change the month number to month name on y axis
plt.yticks(month_num, calendar.month_name[1:13], rotation=20)

# plot horizontal bar graph
plot = plt.barh(month_num, units_sold)

# display the graph on the screen
plt.show()

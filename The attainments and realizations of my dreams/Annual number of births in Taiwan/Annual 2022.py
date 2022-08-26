import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()

fig, ax = plt.subplots()

# Example data
city = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(city))
performance = 3 + 10 * np.random.rand(len(city))
error = np.random.rand(len(city))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=city)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
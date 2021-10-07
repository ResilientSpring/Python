import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = range(2011, 2018)
y = [26.48, 27.56, 29.41, 33.27, 36.32, 37.55, 40.28, 44.35, 48.36, 50.05,
     53.06, 57.39, 62.27, 65.55, 69.17, 74.76, 81.5, 83.18, 86.74, 93.8, 98.75]

plt.plot(y, marker='^', label="Netflix subscribers", linestyle='-')

# get the current axes and store it to ax
ax = plt.gca()

# set ticks in multiples for both labels
ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
# Set major marks every 4 quarters, i.e. once a year

# set minor marks for each quarter
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))

# label the start of each year by Fixed Formatter
ax.get_xaxis().set_major_formatter(ticker.FixedFormatter(x))

plt.legend()
plt.show()

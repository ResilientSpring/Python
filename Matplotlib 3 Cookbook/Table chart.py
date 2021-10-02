import matplotlib.pyplot as plt
import numpy as np

# sold in each year
rows = ['2011', '2012', '2013', '2014', '2015']

# The types of batteries
columns = ('7Ah', '35Ah', '40Ah', '135Ah', '150Ah', '150Ah')

data = [[75, 144, 114, 102, 108],
        [90, 126, 102, 84, 126],
        [96, 114, 75, 105, 135],
        [105, 90, 150, 90, 75],
        [90, 75, 135, 75, 90]]

# Define the range and scale for the y axis.
values = np.arange(0, 600, 100)

# Specify the color spectrum to be used.  Each year will be represented in a different color:
colors = plt.cm.OrRd(np.linspace(0, 0.5, len(rows)))


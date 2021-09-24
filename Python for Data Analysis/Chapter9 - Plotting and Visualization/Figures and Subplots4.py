import matplotlib.pyplot as plt

# When you directly issue a plotting command like the following:
plt.plot([1.5, 3.5, -2, 1.6])
# matplotlib draws on the last figure and subplot used (automatically creating one if necessary),
# thus hiding the figure and subplot creation by you.

plt.show()

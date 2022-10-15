import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

np.random.seed(0)

# Sample random numbers from a normal distribution with mean 1 and standard deviation of 0.1.
x_values = np.random.normal(1, 0.1, 100).astype(np.float)

print("x_values: ", x_values)

y_values = (x_values * (np.random.normal(loc=1, scale=0.05, size=100) - 0.5)).astype(np.float)

print("y_values: ", y_values)

# In order to get assurance that the target and input have a good correlation, plot a scatter plot
# of the two variables:
plt.scatter(x=x_values, y=y_values)
plt.show()

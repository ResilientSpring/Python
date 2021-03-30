import numpy as np

# For random samples from N(\mu, \sigma^2), use:
# sigma * np.random.randn(...) + mu

# Two-by-four array of samples from N(3, 6.25):
array = 3 + 2.5 * np.random.randn(2, 4);
print(array);
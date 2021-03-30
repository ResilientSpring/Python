import numpy as np

condition = np.array([True, False, True, True, False]);

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5]);

yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5]);

# suppose we want to take a value from xarr whenever the corresponding value
# in condition is True, and otherwise take the corresponding value from yarr.
result = np.where(condition, xarr, yarr);

print(result);
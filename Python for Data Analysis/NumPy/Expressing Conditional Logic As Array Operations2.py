import numpy as np

result = np.where(condition=[True, False, True, True, False],
                  x=[1.1, 1.2, 1.3, 1.4, 1.5],
                  y=[2, 3, 4, 5, 6]);

print(result);

# Reference:
# https://numpy.org/doc/stable/reference/generated/numpy.where.html


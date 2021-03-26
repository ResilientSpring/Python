# When arange is used with floating point arguments,
# it is generally not possible to predict the number of elements obtained,
# due to the finite floating point precision.
# For this reason, it is usually better to use the function linspace that receives
# as an argument the number of elements that we want, instead of the step:

import numpy as np
from numpy.core.function_base import linspace

array = linspace(0, 2, 9);  # 9 numbers from 0 to 2
print(array);

x = linspace(0, 2 * np.pi, 100);   # Useful to evaluate function at lots of points.
f = np.sin(x);

print(x, f);


import pandas as pd;
import numpy as np;

# Creating a Series
series = pd.Series([2, -1, 3, 5]);
print(series);

# Series objects behave much like one-dimensional NumPy ndarrays,
# and you can often pass them as parameters to NumPy functions:
array = np.exp(series);

print(array);

# Arithmetic operations on Series are also possible,
# and they apply elementwise, just like for ndarrays:
combination = series + [1000, 2000,3000, 4000];
print(combination);

# Similar to NumPy, if you add a single number to a Series,
# that number is added to all items in the Series. This is called broadcasting:
addition = 1000 + series;
print(addition);

addition = series + 1000;
print(addition);

# The same is true for all binary operations such as * or /, and even conditional operations:
print(addition < 0);
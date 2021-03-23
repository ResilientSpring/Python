import numpy as np;

series = np.arange(1, 11);
print(series);

print(series[1]);

print(series[1:9]);

# Slice indices have useful defaults;
# an omitted first index defaults to zero,
# an omitted second index defaults to the size of the string being sliced.
print(series[:5]);
print(series[5:]);
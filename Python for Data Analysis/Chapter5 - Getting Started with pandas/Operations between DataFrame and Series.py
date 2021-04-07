import numpy as np
import pandas as pd

arr = np.arange(12.).reshape((3, 4));
print(arr);

print(arr[0]);

arr2 = arr - arr[0];
print(arr2);
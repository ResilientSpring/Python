import numpy as np

arr = np.arange(10);
print(arr);

print(arr[5]);

print(arr[5:8]);

arr[5:8] = 12;
print(arr);

arr_slice = arr[5:8];
print(arr_slice);

arr_slice[1] = 12345;
print(arr);
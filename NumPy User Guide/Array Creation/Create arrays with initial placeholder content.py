# Often, the elements of an array are originally unknown, but its size is known.
# Hence, NumPy offers several functions to create arrays with initial placeholder content.
# These minimize the necessity of growing arrays, an expensive operation.

import numpy as np

# The function zeros creates an array full of zeros,
array1 = np.zeros((3, 4));
print(array1);

# the function ones creates an array full of ones,
array2 = np.ones((2, 3, 4), dtype=np.int16);
print(array2);

# and the function empty creates an array whose initial content is random and depends on
# the state of the memory.
array3 = np.empty((2, 3));
print(array3);

# By default, the dtype of the created array is float64,
# but it can be specified via the key word argument dtype.

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#array-creation
# Some operations, such as += and *=, act in place to modify an existing array
# rather than create a new one.

import numpy as np;

a = np.ones((2, 3), dtype=int);

print(a);

a *= 3;
print(a);

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#basic-operations
# The criterion to satisfy for providing the new shape is that
# 'The new shape should be compatible with the original shape'

# Python allow us to give one of new shape parameter as -1 (eg: (2,-1) or (-1,3) but not (-1, -1)).
# It simply means that it is an unknown dimension and we want Python to figure it out.

# And Python will figure this by looking at the 'length of the array and remaining dimensions'
# and making sure it satisfies the above mentioned criteria.

# Reference: https://stackoverflow.com/a/42510505/14900011

# Now see the example.

import numpy as np

z = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print(z.shape)

# Now, reshape the array z with (-1) . The resultant new shape is (12,) and is compatible with the
# original shape (3,4).
z1 = z.reshape(-1)

print(z1)

# Now, reshape the array z with (-1, 1) .
# We have provided column as 1 but rows as unknown .
z2 = z.reshape(-1, 1)

# So we get the result new shape as (12, 1). Again, it is compatible with the original shape(3,4).
print(z2)

# The above is consistent with numpy advice/error message,
# to use reshape(-1,1) for a single feature; i.e. single column
# Nutshell: Reshape your data using reshape(-1, 1) if your data has a single feature.

# New shape as (-1, 2). row unknown, column 2.
z3 = z.reshape(-1, 2)

# We get result new shape as (6, 2)
print(z3)
print(z3.shape)

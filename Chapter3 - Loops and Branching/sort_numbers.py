# Exercise 3.10 on page 76 of the textbook.

# Use the uniform function from the random module to generate an array of 6 random numbers
# between 0 and 10. The program should then sort the array so that numbers appear in
# increasing order.
# Let the program make a formatted print of the array to screen before and after sorting.

import numpy as np

r = np.random.uniform(0, 11, 6);
print("Before sorting: ");
print(r);

r = np.sort(r);
print("After sorting: ");
print(r);

# Reference:
# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order
# Exercise on page 74 of the textbook.

n = 5;
h = [1.60, 1.85, 1.75, 1.80, 0.50];

i = 0;
sum = 0;

# As to logical operators in python, see: https://www.w3schools.com/python/python_operators.asp
while ( i < 5) :
    sum += h[i];
    i += 1;
    # Python doesn't support ++, but you can do: number += 1
    # Reference: https://stackoverflow.com/questions/2632677/python-integer-incrementing-with

average = sum / n;

print("Average is {:.2f} centimeter.".format(average));

# Double precision floating values in Python? [closed]

# Python's built-in float type has double precision
# (it's a C double in CPython, a Java double in Jython).
# If you need more precision, get NumPy and use its numpy.float128.
# Reference: https://stackoverflow.com/a/6663292/14900011
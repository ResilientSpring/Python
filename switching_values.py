# Exercise on page 57 of the textbook.
from numpy import linspace

x = linspace(1, 3, 3);
print(x);

intermediate = x[0];
x[0] = x[1];
x[1] = intermediate;

print(x);
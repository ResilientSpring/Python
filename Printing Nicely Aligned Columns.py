# Example on page 31 of the textbook
# Print a column of t values together with associated function values g(t) = t sin(t) in a
# second column.
from math import sin

t0 = 2;
dt = 0.55;

t = t0 + 0 * dt; g = t * sin(t);
print("{:6.2f} {:8.3f}".format(t, g));

t = t0 + 1 * dt; g = t * sin(t);
print("{:6.2f} {:8.3f}".format(t, g));

t = t0 + 2 * dt; g = t * sin(t);
print("{:6.2f} {:8.3f}".format(t, g));

print("formatted output versus a simple call to print(t, g)");

t = t0 + 0 * dt; g = t * sin(t);
print(t, g);

t = t0 + 1 * dt; g = t * sin(t);
print(t, g);

t = t0 + 2 * dt; g = t * sin(t);
print(t, g);
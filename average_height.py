# Example on page 62 of the textbook
from numpy import zeros

N = 5;
h = zeros(N);  # heights of family members (in meter)
h[0] = 1.60; h[1] = 1.85; h2 = 1.75; h[3] = 1.80; h[4] = 0.50;

sum = 0;
for i in [0, 1, 2, 3, 4]:
    sum = sum + h[i];

average = sum/N;

print("Average height: {:g} meter".format(average));

average2 = ( h[0] + h[1] + h[2] + h[3] + h[4]  ) / 5;
print("Average height calcuated by hand: {:f} meters".format(average2));
# Exercise 3.11 on page 76 of the textbook.
from math import sqrt

pi_of_Leibniz = 0;

pi_of_Euler = 0;

N = int(input("Input the number of iteration N: "));

for k in range(0, N, 1):

    pi_of_Leibniz = ( 1 / (4 * k + 1) * (4 * k + 3) ) * 8;

for K in range(1, N, 1):

    squared = 6 * (1 / K ** 2);

    pi_of_Euler = sqrt(squared);
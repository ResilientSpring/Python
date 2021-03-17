# Exercise 3.11 on page 76 of the textbook.
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

pi = 3.14159265359;

pi_of_Leibniz = 0;

pi_of_Euler = 0;

N = int(input("Input the number of iteration N: "));

x = np.zeros(N + 1, dtype=float);
y = np.zeros(N + 1, dtype=float);

for k in range(0, N, 1):

    pi_of_Leibniz = ( 1 / (4 * k + 1) * (4 * k + 3) ) * 8;
    x[k] = pi_of_Leibniz;

for K in range(1, N, 1):

    squared = 6 * (1 / K ** 2);

    pi_of_Euler = sqrt(squared);
    y[K] = pi_of_Euler;

plt.plot(pi, x, 'r--', pi, )
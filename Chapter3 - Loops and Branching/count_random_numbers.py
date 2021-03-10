# Exercise 3.7 on page 75 of the textbook.
import random
import numpy

N = int(input("How many random integers do you want from 1 to 6?"));
collection = numpy.zeros(N, dtype=int);
M = 0;

for i in range(0, len(collection)-1, 1):
    collection[i] = random.randint(1, 6);

for i in range(0, len(collection), 1):

    if (collection[i] == 6) :
        M += 1;
division = M / N;

print("There are {:d} numbers equal to 6; M/N = {:g}.".format(M, division));
print("Elements of random array: ")
print(collection);
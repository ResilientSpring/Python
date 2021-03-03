import random

a = 1;
b = 6;

r1 = random.randint(a, b);  # first die
r2 = random.randint(a, b);  # second die

print("The dice gave: {:d} and {:d}".format(r1, r2));

r3 = random.randint(12,34);
r4 = random.randint(56, 78);

print("The dice gave: {:d} and {:d}".format(r3, r4));

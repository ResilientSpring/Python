# Example on page 73 of the textbook.

import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000;  # number of steps.
d = 1;  # step length (e.g., in meter.)
x = np.zeros(N + 1);  # x coordinates  e.g., x[0, 0 , 0, ..., x1001]
y = np.zeros(N + 1);  # y coordinates
x[0] = 0;
y[0] = 0;  # set initial position

for i in range(0, N, 1):
    r = random.random();  # random number in [0,1)
    if 0 <= r < 0.25:  # move north
        y[1 + i] = y[i] + d;           # Starting from y[1] since y[0] has been set to 0.
        x[1 + i] = x[i];
    elif 0.25 <= r < 0.5:  # move east
        x[1 + i] = x[i] + d;           # X-axis is west-east bound.
        y[1 + i] = y[i];
    elif 0.5 <= r < 0.75:  # move south
        y[1 + i] = y[i] - d;           # Y-axis is north-south bound.
        x[1 + i] = x[i];
    else:                  # move west
        x[1 + i] = x[i] - d;
        y[1 + i] = y[i];

# plot path (mark start and stop with blue o and *, respectively)
plt.plot(x, y, 'r--', x[0], y[0], 'bo', x[-1], y[-1], 'b*');
plt.xlabel("x"); plt.ylabel("y");
plt.show();

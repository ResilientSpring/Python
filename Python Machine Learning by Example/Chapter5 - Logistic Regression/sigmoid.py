import numpy as np
import matplotlib.pyplot as plt


def sigmoid(input):
    return 1.0 / (1 + np.exp(- input));

Z = np.linspace(-8, 8, 1000);
y = sigmoid(Z);

plt.plot(Z, y);
plt.axhline(y=0, ls="dotted", color='k');
plt.axhline(y=0.5, ls="dotted", color='k');
plt.yticks([0.0, 0.25, 0.5, 0.75, 1.0])
plt.xlabel('z')
plt.ylabel('y(z)')

plt.savefig("sigmoid.jpg")

plt.show()
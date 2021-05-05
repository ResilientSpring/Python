import matplotlib.pyplot as plt
import numpy as np

pos_fraction = np.linspace(0.00, 1.00, 1000)

entropy = - (pos_fraction * np.log2(pos_fraction) + (1 - pos_fraction) * np.log2(1 - pos_fraction))

plt.plot(pos_fraction, entropy)

plt.xlabel("Positive fraction")
plt.ylabel("Entropy")

plt.ylim(0, 1)

plt.savefig("Entropy.jpg")

plt.show()

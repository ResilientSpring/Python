import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z));

# ### Learning the weights of the logistic cost function

def cost_1(z):
    return - np.log(sigmoid(z));

def cost_0(z):
    return - np.log(1 - sigmoid(z));


z = np.arange(-10, 10, 0.1);
phi_z = sigmoid(z);

c1 = [cost_1(x) for x in z];
plt.plot(phi_z, c1, label="J(W) if y = 1");

c0 = [cost_0(x) for x in z];
plt.plot(phi_z, c0, linestyle='--', label="J(W) if y = 0");

plt.ylim(0.0, 5.1);
plt.xlim([0, 1]);
plt.xlabel("$\phi$(z)");
plt.ylabel("J(W)");
plt.legend(loc="best");

plt.tight_layout();

plt.savefig("logistic_cost_function.jpg");

plt.show();
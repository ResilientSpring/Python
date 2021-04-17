import numpy as np
import matplotlib.pyplot as plt

y_hat = np.linspace(0, 1, 1000);

cost = - np.log(1 - y_hat);
plt.plot(y_hat, cost);
plt.xlabel("Prediction");

plt.ylabel("Cost");
plt.xlim(0, 1);
plt.ylim(0, 7);

plt.savefig("cost_function_class_0.jpg");

plt.show();
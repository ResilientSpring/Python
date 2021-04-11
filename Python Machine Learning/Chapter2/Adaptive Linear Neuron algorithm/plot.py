import numpy as np
import AdalineGD
import matplotlib.pyplot as plt
import pandas as pd
import dataset as training_set

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4));
ada1 = AdalineGD.AdalineGD(n_iter=10, eta=0.01).fit(X=training_set.X, y=training_set.y);
ax[0].plot(range(1, len(ada1.cost_) + 1), np.log10(ada1.cost_), marker='o');
ax[0].set_xlabel("Epochs");
ax[0].set_ylabel("long(Sum-squared-error");
ax[0].set_title("Adaline - Learning rate 0.01");

ada2 = AdalineGD.AdalineGD(n_iter=10, eta=0.0001).fit(X=training_set.X, y=training_set.y);
ax[1].plot(range(1, len(ada2.cost_) + 1), ada2.cost_, marker='o');
ax[1].set_xlabel("Epochs");
ax[1].set_ylabel("Sum-squared-error");
ax[1].set_title("Adaline - Learning rate 0.0001");
plt.show();
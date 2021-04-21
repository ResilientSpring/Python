import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
import L1_regularization_and_sparsity as L1
import wine_dataset

fig = plt.figure()
ax = plt.subplot(111)
colors = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "pink", "lightgreen",
          "lightblue", "gray", "indigo", "orange"]

weights, params = [], []

for c in np.arange(-4., 6.):
    lr = LogisticRegression(penalty='l1', C=10. ** c, solver="liblinear", multi_class="ovr",
                            random_state=0)

    lr.fit(X=L1.X_train_std, y=L1.y_train)
    weights.append(lr.coef_[1])
    params.append(10**c)

weights = np.array(weights)

for column, color in zip(range(weights.shape[1]), colors):
    plt.plot(params, weights[:, column], label=wine_dataset.df.columns[column + 1], color=color)

plt.axhline(0, color="black", linestyle="--", linewidth=3)
plt.xlim([10**(-5), 10**5])
plt.ylabel("weight coefficient")
plt.xlabel('C')
plt.xscale("log")
plt.legend(loc="upper left")
ax.legend(loc="upper center", bbox_to_anchor=(1.38, 1.03), ncol=1, fancybox=True)

plt.savefig("The weight coefficients of the different features for different regularization strengths.jpg")

plt.show()
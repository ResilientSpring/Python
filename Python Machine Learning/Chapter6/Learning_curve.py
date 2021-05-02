import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import Data_pre_processing as dataset
import numpy as np
from numpy.core.function_base import linspace

pipe_lr = make_pipeline(StandardScaler(), LogisticRegression(penalty='l2', random_state=1,
                                                             solver='lbfgs', max_iter=10000))

train_sizes, train_scores, test_scores = \
    learning_curve(estimator=pipe_lr, X=dataset.X, y=dataset.y, shuffle=True,
                   train_sizes=linspace(0.1, 1.0, 10), scoring="accuracy",
                   cv=10)

print(train_scores)
print(test_scores)

train_mean = np.nanmean(train_scores, axis=1)
train_std = np.nanstd(train_scores, axis=1)
test_mean = np.nanmean(test_scores, axis=1)
test_std = np.nanstd(test_scores, axis=1)
# np.nanmean() differs from np.mean() in that it Compute the arithmetic mean along the
# specified axis in a multi-dimensional array, ignoring NaNs. [1][2]

plt.plot(train_sizes, train_mean, color="blue", marker='o', markersize=5,
         label="Training accuracy")
plt.fill_between(x=train_sizes, y1=train_mean + train_std, y2=train_mean - train_std,
                 alpha=0.15, color="blue")

plt.plot(train_sizes, test_mean, color="green", linestyle="--", marker="s", markersize=5,
         label="Validation accuracy")
plt.fill_between(x=train_sizes, y1=test_mean + test_std, y2=test_mean - test_std,
                 alpha=0.15, color="green")

plt.grid()

plt.xlabel("Number of training examples")
plt.ylabel("Accuracy")

plt.legend(loc="lower right")

plt.ylim([0.8, 1.03])

plt.savefig("learning_curve.jpg")

plt.show()

# Reference:
# 1. https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html
# 2. https://numpy.org/doc/stable/reference/generated/numpy.mean.html
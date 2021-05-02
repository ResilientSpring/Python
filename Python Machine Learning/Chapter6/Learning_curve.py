import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import Data_pre_processing as dataset
import numpy as np
from numpy.core.function_base import linspace

train_sizes = linspace(0.1, 1.0, 10)

pipe_lr = make_pipeline(StandardScaler(), LogisticRegression(penalty='l2', random_state=1,
                                                             solver='lbfgs', max_iter=10000))

train_scores, test_scores = learning_curve(estimator=pipe_lr, X=dataset.X, y=dataset.y,
                                           shuffle=True, train_sizes=train_sizes, cv=10)

train_mean = train_scores.mean()
train_std = train_scores.std()
test_mean = test_scores.mean()
test_std = test_scores.std()

plt.plot(train_sizes, train_mean, color="blue", marker='o', markersize=5, label="Training accuracy")
plt.fill_between(x=train_sizes, y1=train_mean + train_std, y2=train_mean - train_std, alpha=0.15, color="blue")
plt.plot(train_sizes, test_mean, color="green", linestyle="--", marker="s", markersize=5, label="Validation accuracy")
plt.fill_between(x=train_sizes, y1=test_mean + test_std, y2=test_mean - test_std, alpha=0.15, color="green")
plt.grid()
plt.xlabel("Number of training examples")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.ylim([0.8, 1.03])
plt.show()
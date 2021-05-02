from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import Data_pre_processing as dataset
import numpy as np

pipe_lr = make_pipeline(StandardScaler(), LogisticRegression(penalty='l2', random_state=1,
                                                             solver='lbfgs', max_iter=10000))

param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]

train_scores, test_scores = validation_curve(estimator=pipe_lr, X=dataset.X, y=dataset.y,
                                             param_name='logisticregression__C',
                                             param_range=param_range, cv=10)

print(train_scores)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(param_range, train_mean, color='blue', marker='o', markersize=5,
         label='Training accuracy')

plt.fill_between(x=param_range, y1=train_mean + train_std, y2=train_mean - train_std,
                 alpha=0.15, color='blue')

plt.plot(param_range, test_mean, color='green', linestyle='--', marker='s', markersize=5,
         label='Validation accuracy')

plt.fill_between(x=param_range, y1=test_mean + test_std, y2=test_mean - test_std, alpha=0.15,
                 color='green')

plt.grid()
plt.xscale('log')
plt.legend(loc='lower right')
plt.xlabel('Parameter C')
plt.ylabel('Accuracy')
plt.ylim([0.8, 1.0])

plt.savefig("Validation_curves.jpg")

plt.show()

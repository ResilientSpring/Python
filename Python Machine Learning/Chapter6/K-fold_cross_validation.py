import Data_pre_processing as dataset
from sklearn.model_selection import cross_val_score
import numpy as np

scores = cross_val_score(estimator=dataset.pipe_lr, X=dataset.X_train, y=dataset.y_train,
                         cv=10, n_jobs=1)
print(scores)

mean = np.mean(scores)

std_deviation = np.std(scores)

print(mean)

print(std_deviation)
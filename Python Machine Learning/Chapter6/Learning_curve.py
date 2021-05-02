import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import Data_pre_processing as dataset
import numpy as np

pipe_lr = make_pipeline(StandardScaler(), LogisticRegression(penalty='l2', random_state=1,
                                                             solver='lbfgs', max_iter=10000))

train_scores, test_scores = learning_curve(estimator=pipe_lr, X=dataset.X, y=dataset.y,
                                           shuffle=True, train_sizes=np.linspace(0.1, 1.0, 10),
                                           cv=10)

train_mean = train_scores.mean()
train_std = train_scores.std()
test_mean = test_scores.mean()
test_std = test_scores.std()

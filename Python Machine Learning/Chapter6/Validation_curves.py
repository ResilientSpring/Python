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

train_scores, test_scores = validation_curve(estimator=pipe_lr, X=dataset.X, y=dataset.y)
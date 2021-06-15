'''
Source codes for Python Machine Learning By Example 3rd Edition (Packt Publishing)
Chapter 5 Predicting Online Ads Click-through with Logistic Regression
Author: Yuxi (Hayden) Liu (yuxi.liu.ece@gmail.com)
'''

import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import SGDClassifier
import pandas as pd

# Online learning

n_rows = 100000 * 11
df = pd.read_csv("trainee.csv", nrows=n_rows)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1).values
Y = df['click'].values

n_train = 100000 * 10
X_train = X[:n_train]
Y_train = Y[:n_train]
X_test = X[n_train:]
Y_test = Y[n_train:]

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(X_train)

# The number of iterations is set to 1 if using partial_fit.
sgd_lr_online = SGDClassifier(loss='log', penalty=None, fit_intercept=True, max_iter=1, learning_rate='constant',
                              eta0=0.01)

import timeit

start_time = timeit.default_timer()

# Use the first 1,000,000 samples for training, and the next 100,000 for testing
for i in range(9):
    x_train = X_train[i * 100000:(i + 1) * 100000]
    y_train = Y_train[i * 100000:(i + 1) * 100000]
    x_train_enc = enc.transform(x_train)
    sgd_lr_online.partial_fit(x_train_enc.toarray(), y_train, classes=[0, 1])

print(f"--- {(timeit.default_timer() - start_time)}.3fs seconds ---")

x_test_enc = enc.transform(X_test)

pred = sgd_lr_online.predict_proba(x_test_enc.toarray())[:, 1]
print(f'Training samples: {n_train * 10}, AUC on testing set: {roc_auc_score(Y_test, pred):.3f}')

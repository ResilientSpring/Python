'''
Source codes for Python Machine Learning By Example 3rd Edition (Packt Publishing)
Chapter 4 Predicting Online Ads Click-through with Tree-Based Algorithms
Author: Yuxi (Hayden) Liu (yuxi.liu.ece@gmail.com)
'''

import pandas as pd

n_rows = 300000
df = pd.read_csv("train.csv", nrows=n_rows)
print(df.head(5))

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1).values
Y = df['click'].values

print(X.shape)

n_train = int(n_rows * 0.9)
X_train = X[:n_train]
Y_train = Y[:n_train]
X_test = X[n_train:]
Y_test = Y[n_train:]

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
X_train_enc = enc.fit_transform(X_train)

print(type(X_train_enc))

print(X_train_enc[0])

X_test_enc = enc.transform(X_test)

from sklearn.tree import DecisionTreeClassifier

parameters = {'max_depth': [3, 10, None]}
decision_tree = DecisionTreeClassifier(criterion='gini', min_samples_split=30)

from sklearn.model_selection import GridSearchCV

grid_search = GridSearchCV(decision_tree, parameters, n_jobs=-1, cv=3, scoring='roc_auc')

grid_search.fit(X_train_enc, Y_train)
print(grid_search.best_params_)

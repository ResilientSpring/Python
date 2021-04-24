import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import Breast_cancer_Wisconsin_dataset as dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

X = dataset.df.loc[:, 2:].values
print(X)

y = dataset.df.loc[:, 1]. values
print(y)

le = LabelEncoder()

y = le.fit_transform(y)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,
                                                    stratify=y, random_state=1)

pipe_lr = make_pipeline(StandardScaler(), PCA(n_components=2),
                        LogisticRegression(random_state=1, solver="lbfgs"))

pipe_lr.fit(X=X_train, y=y_train)

y_prediction = pipe_lr.predict(X=X_test)

print("Test Accuracy: {:.3f}".format(pipe_lr.score(X=X_test, y=y_test)))
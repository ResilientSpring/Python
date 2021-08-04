import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# importing the dataset
iris_df = sns.load_dataset("iris");

print(iris_df.head())

# Creating feature set
X = iris_df.drop(["species"], axis=1)

# Creating label set
y = iris_df["species"]

# Converting labels to numbers
le = LabelEncoder()
y = le.fit_transform(y)

# Dividing data into 80-20% training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# applying scaling on training and test data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Creating object of PCA class
pca = PCA()

# Training PCA model on training data
X_train_PCAed = pca.fit_transform(X_train)

# Making predictions on test data
X_test_PCAed = pca.transform(X_test)

print(X_train_PCAed)
print('=' * 30)
print(X_test_PCAed)
print('=' * 30)

# How much variance does the first, second, third, and fourth principal component cause?
variance_ratio = pca.explained_variance_ratio_
print(variance_ratio)

# According to the variance_ratio, select the two principal components that caused a
# collective variance of 96.19% (72.22% + 23.97% = 96.19%)
pca2 = PCA(n_components=2)

X_train = pca2.fit_transform(X_train)
X_test = pca2.transform(X_test)

logistic_regression = LogisticRegression()
logistic_regression.fit(X=X_train, y=y_train)

y_prediction = logistic_regression.predict(X=X_test)

print(accuracy_score(y_true=y_test, y_pred=y_prediction))

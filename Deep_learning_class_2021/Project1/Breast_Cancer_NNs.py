from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import numpy as np
import keras

cancer_data = load_breast_cancer()

X = cancer_data.data
y = cancer_data.target

print('Input data size: ', X.shape)
print('Output data size: ', y.shape)

# Check to see if it's a binary or multi-class classification.
print('Label names: ', cancer_data.target_names)

# Determine if the data distribution among the dataset is balanced.
n_positive = (y == 1).sum()
n_negative = (y == 0).sum()
print(f'{n_positive} positive samples and {n_negative} negative samples.')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.33)

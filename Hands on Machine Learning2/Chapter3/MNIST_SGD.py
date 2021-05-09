import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

url = "https://media.githubusercontent.com/media/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/mnist_train.csv"

MNIST_training_set = pd.read_csv(filepath_or_buffer=url, header=None)
print(MNIST_training_set.head(n=100))

# Feature set
features_train = MNIST_training_set.iloc[1:, 1:]
print(features_train)

# Label set
labels_train = MNIST_training_set.iloc[1:, 0]
print(labels_train)

test_set_url  = "https://media.githubusercontent.com/media/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/mnist_test.csv"
MNIST_test_set = pd.read_csv(filepath_or_buffer=test_set_url, header=None)
print(MNIST_test_set.head(n=100))

# Test feature set
features_test = MNIST_test_set.iloc[1:, 1:]
print(features_test)

# Test label set
labels_test = MNIST_test_set.iloc[1:, 0]
print(labels_test)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X=features_train, y=labels_train)

y_prediction = sgd_clf.predict(X=features_test)

print(classification_report(y_true=labels_test, y_pred=y_prediction))

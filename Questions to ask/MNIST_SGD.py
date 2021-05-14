import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

url = "https://media.githubusercontent.com/media/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/mnist_train.csv"

MNIST_training_set_full = pd.read_csv(filepath_or_buffer=url, header=None)
print(MNIST_training_set_full.head(n=100))

MNIST_training_set = pd.read_csv(filepath_or_buffer=url, header=None, dtype=float, skiprows=1)
print(MNIST_training_set.head(n=100))

# Feature set
features_train = MNIST_training_set.iloc[1:, 1:]
print(features_train)
print(type(features_train))
print(features_train.dtypes)

numeric_features_train = features_train.to_numpy()
print(numeric_features_train)

# Label set
labels_train = MNIST_training_set.iloc[1:, 0]
print(labels_train)
print(type(labels_train))

numeric_labels_train = labels_train.to_numpy()
print(numeric_labels_train)

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
sgd_clf.fit(X=numeric_features_train, y=numeric_labels_train)

y_prediction = sgd_clf.predict(X=features_test)

print(classification_report(y_true=labels_test, y_pred=y_prediction))

# Question: How to resolve "TypeError: '<' not supported between instances of 'int' and 'str'"
# The copy on my Colab: MNIST_SGD.ipynb

# I searched Google: https://www.google.com/search?q=%27%3C%27+not+supported+between+instances+of+%27int%27+and+%27str%27&oq=%27%3C%27+not+supported+between+instances+of+%27int%27+and+%27str%27&aqs=chrome..69i57j0l4j0i22i30l5.1166j0j7&sourceid=chrome&ie=UTF-8
# I searched StackOverflow: https://stackoverflow.com/questions/41950021/typeerror-not-supported-between-instances-of-str-and-int
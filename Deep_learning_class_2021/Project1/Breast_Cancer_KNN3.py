from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
dataset = load_breast_cancer()
print(dataset) # Check the dataset to see its content arrangement.

target_names = dataset.target_names
print(target_names)

# Organize our data
label_names = dataset["target_names"]

# Check to see if it's a binary or multi-class classification.
## Print the size of the label set first since it could be several thousands in length; it would be
## inefficient to manually see through a long set to determine the number of distinct classes
## within a single label set.
labels = dataset["target"]
print(labels.shape)

# What the features are?
feature_name = dataset["feature_names"];

# How many features does one instance have?
features = dataset["data"];
print(features.shape)

# Look at our data
print(label_names);
print(labels[0]);
print(feature_name[0]);
print(features[0]);

# Split our data (divide data into Training and Test sets)
train, test, train_label, test_labels = train_test_split(features, labels, test_size=0.33,
                                                         random_state=42);

knn_clf = KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X=train, y=train_label)

y_prediction = knn_clf.predict(X=test)

print("Accuracy Score: ", accuracy_score(y_true=test_labels, y_pred=y_prediction))

print("Classification report: ", '\n', classification_report(y_true=test_labels,
                                                             y_pred=y_prediction,
                                                             target_names=target_names))

scores = cross_val_score(estimator=knn_clf, X=train, y=train_label, cv=10,
                         scoring='accuracy')

print("10-fold Cross Validation Scores: ", scores)
print("Mean Scores: ", scores.mean())

y_prediction2 = knn_clf.predict(X=train)

print("Classification report after 10-fold cross validation: ", '\n',
      classification_report(y_true=train_label,
                            y_pred=y_prediction2,
                            target_names=target_names))
print("Accuracy: ", accuracy_score(y_true=train_label, y_pred=y_prediction2))

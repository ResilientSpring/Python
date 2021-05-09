from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import numpy as np

# Load dataset
data = load_breast_cancer()
print(data)

target_names = data.target_names
print(target_names)

# Organize our data
label_names = data["target_names"];
labels = data["target"];
feature_name = data["feature_names"];
features = data["data"];

# Look at our data
print(label_names);
print(labels[0]);
print(feature_name[0]);
print(features[0]);

# Split our data (divide data into Training and Test sets)
train, test, train_label, test_labels = train_test_split(features, labels, test_size=0.33,
                                                         random_state=42);

tree_classifier = DecisionTreeClassifier(max_depth=5)
tree_classifier.fit(X=train, y=train_label)

y_prediction = tree_classifier.predict(X=test)

print("Accuracy Score: ", accuracy_score(y_true=test_labels, y_pred=y_prediction))

target_name = np.array(['malignant', 'benign'])

print("Classification report: ", '\n', classification_report(y_true=test_labels,
                                                             y_pred=y_prediction,
                                                             target_names=target_names))

scores = cross_val_score(estimator=tree_classifier, X=train, y=train_label, cv=10,
                         scoring='accuracy')

print("10-fold cross validation Scores: ", scores)
print("Mean Scores: ", scores.mean())

y_prediction2 = tree_classifier.predict(X=train)

print("Classification report after 10-fold Cross validation: ", '\n',
      classification_report(y_true=train_label,
                            y_pred=y_prediction2,
                            target_names=target_names))

print("Accuracy: ", accuracy_score(y_true=train_label, y_pred=y_prediction2))

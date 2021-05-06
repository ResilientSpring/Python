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


from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer();
print(data);

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
train, test, train_label, test_labels = train_test_split(features, labels, test_size=0.33, random_state=42);

# Initialize our classifier
gnb = GaussianNB();

# Train our classifier
model = gnb.fit(X=train, y=train_label);

# Make predictions
y_prediction = gnb.predict(X=test);

print(y_prediction);

# Evaluate accuracy
print(accuracy_score(y_true=test_labels, y_pred=y_prediction));
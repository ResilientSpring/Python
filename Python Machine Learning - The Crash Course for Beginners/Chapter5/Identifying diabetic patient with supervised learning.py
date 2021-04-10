import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# [1]
from sklearn.impute import SimpleImputer

patient_data = pd.read_csv(filepath_or_buffer="patients.csv")
print(patient_data);

featuers_set = patient_data.iloc[0:12, 0:3];
print(featuers_set);

featuers_set_np = featuers_set.to_numpy();
print(featuers_set_np);

# Construct the object of the Imputer Class.
imputer_mean = SimpleImputer(missing_values=np.nan, strategy="mean");
imputer_mean = imputer_mean.fit(X=featuers_set_np[:, 1]);
featuers_set_np[:, 1] = imputer_mean.transform(X=featuers_set_np[:, 1]);
print(featuers_set_np);

# Convert categorical data to numbers
label_encoder_features = LabelEncoder();
featuers_set_np[ : , 2] = label_encoder_features.fit_transform(y=featuers_set_np[:, 2]);
labels = label_encoder_features.fit_transform(y=featuers_set_np[:, 3]);

# Divide data into training and test sets.
train_features, test_features, train_labels, test_labels = \
    train_test_split(featuers_set_np, labels, test_size=0.25, random_state=0);

# Construct the object.
feature_scaler = StandardScaler();
train_features = feature_scaler.fit_transform(X=train_features);
train_features = feature_scaler.fit_transform(X=train_features);
test_features = feature_scaler.fit_transform(X=test_features);

linear_regression = LinearRegression();
regressor = linear_regression.fit(X=train_features, y=train_labels);

# making predictions on test set
y_prediction = linear_regression.predict(X=test_features);

print("Mean absolute value:", metrics.accuracy_score(y_true=test_labels, y_pred=y_prediction));

# References:
# 1. https://scikit-learn.org/stable/modules/impute.html
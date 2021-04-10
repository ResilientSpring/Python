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

labels = patient_data.iloc[:, 3];
print(labels);

labels_np = labels.to_numpy();
print(labels_np);

# Construct the object of the Imputer Class.
imputer_mean = SimpleImputer(missing_values=np.nan, strategy="mean");
imputer_mean = imputer_mean.fit(X=featuers_set_np[:, 1:2]);
featuers_set_np[:, 1:2] = imputer_mean.transform(X=featuers_set_np[:, 1:2]);
print(featuers_set_np);

# Convert categorical data to numbers
label_encoder_features = LabelEncoder();

## Convert sexes into 1 and 0
featuers_set_np[:, 2] = label_encoder_features.fit_transform(y=featuers_set_np[:, 2]);
print(featuers_set_np);

## Convert Yes and No into 1 and 0
labels_np_numerical = label_encoder_features.fit_transform(y=labels_np);
print(labels_np_numerical);

train_features, test_features, train_labels, test_labels = \
    train_test_split(featuers_set_np, labels_np_numerical, test_size=0.25, random_state=0);

# Normalizing the value
## Initialize the scaler
feature_scaler = StandardScaler();

## Assign the normalized values to the training feature set.
train_features = feature_scaler.fit_transform(X=train_features);

## Assign the normalized values to the test feature set.
test_features = feature_scaler.fit_transform(X=test_features);

# Note that there isn't really a need for you to scale labels on any of your classification problems.
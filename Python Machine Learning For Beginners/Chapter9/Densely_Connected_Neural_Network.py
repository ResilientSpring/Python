import seaborn as sns
import pandas as pd
import numpy as np
from keras.layers import Dense, Dropout, Activation
from keras.models import Model, Sequential
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

url = "https://raw.githubusercontent.com/AbhiRoy96/Banknote-Authentication-UCI-Dataset/master/bank_notes.csv"

banknote_data = pd.read_csv(filepath_or_buffer=url)
print(banknote_data)

# Plot a count plot to see the distribution of data with respect to the values in the class that we want to predict
sns.countplot(x="Target", data=banknote_data)

# Divide the dataset into features and target labels.

## Feature set
X = banknote_data.drop(["Target"], axis=1)
print(X)

## Class set
y = banknote_data.filter(["Target"], axis=1)
print(y)

# Divide Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Scale the data
sc = StandardScaler()
X_train = sc.fit_transform(X=X_train)
X_test = sc.transform(X=X_test)


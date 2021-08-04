import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# importing the dataset
iris_df = sns.load_dataset("iris");

print(iris_df.head())

# Creating feature set
X = iris_df.drop(["species"], axis=1)

# Creating label set
y = iris_df["species"]

# Converting labels to numbers
le = LabelEncoder()
y = le.fit_transform(y)

# Dividing data into 80-20% training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# applying scaling on training and test data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Creating object of PCA class
pca = PCA()

# Training PCA model on training data
pca.fit_transform(X_train)

# Making predictions on test data
pca.transform(X_test)



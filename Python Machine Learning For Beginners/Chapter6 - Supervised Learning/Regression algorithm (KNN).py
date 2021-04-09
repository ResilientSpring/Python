import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics

print(sns.get_dataset_names());

tips_df = sns.load_dataset("tips");
print(tips_df.head());

# Copy obj where its index is dropped/removed.
X = tips_df.drop(axis=1, labels="tip");

# feature set
print(X);

y = tips_df["tip"];

# record set
print(y);

print(type(X));
numerical = X.drop(axis=1, labels=["sex", "smoker", "day", "time"]);
print(numerical);

# Create a dataframe that contains only categorical columns.
categorical = X.filter(axis=1, items=["sex", "smoker", "day", "time"]);
print(categorical);

categorical_numerical = pd.get_dummies(data=categorical, drop_first=True);
print(categorical_numerical);

X1 = pd.concat([numerical, categorical_numerical], axis=1);
print(X1);

X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.20, random_state=0);

sc = StandardScaler();

# scaling the training set
X_train = sc.fit_transform(X=X_train);

# scaling the test set
X_test = sc.transform(X=X_test);

KNN_reg = KNeighborsRegressor(n_neighbors=5);
regressor = KNN_reg.fit(X=X_train, y=y_train);

y_prediction = regressor.predict(X_test);

print("Mean Absolute Error:", metrics.mean_absolute_error(y_true=y_test, y_pred=y_prediction));
print("Mean Squared Error:", metrics.mean_squared_error(y_true=y_test, y_pred=y_prediction));
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_true=y_test, y_pred=y_prediction)));
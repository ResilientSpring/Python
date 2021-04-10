import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import Data_preprocessing as data_ready

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

# pick the 100th record from our dataset.
the_100th_record = tips_df.iloc[100];

print(the_100th_record);

# Predict the value of the tip of the 100th record using the random forest regressor algorithm.
from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(n_estimators=500, random_state=42);
regressor = rf_reg.fit(X=data_ready.X_train, y=data_ready.y_train);

## Data scaling/normalization
sc = StandardScaler();

single_record = sc.transform(X=data_ready.X1.values[100].reshape(1, -1));
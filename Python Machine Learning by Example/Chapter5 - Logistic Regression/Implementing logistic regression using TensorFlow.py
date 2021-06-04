import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Read in the first 6000 rows.
df = pd.read_csv('train.csv', nrows=6000)
print(df)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)
print(X)

y = df['click']
print(y)

X_train = X[: int(6000 * 0.9)] # Use 90% of the read-in rows for training.
y_train = y[: int(6000 * 0.9)]

X_test = X[int(6000 * 0.9) :]
y_test = y[int(6000 * 0.9) :]

# Because Pandas Dataframe can't recognize 6000 * 0.9 in [:], we need to break down the steps.
# number_of_rows = 6000 * 0.9

# X_train = X[:number_of_rows]
# y_train = y[:number_of_rows]

# X_test = X[number_of_rows:]
# y_test = y[number_of_rows:]

# Convert Pandas.Dataframe to NumPy array because Tensor is only compatible with NumPy array.
X_train = X_train.to_numpy()
y_train = y_train.to_numpy().astype('float32')

print(X_train)

X_test = X_test.to_numpy()
y_test = y_test.to_numpy().astype('float32')

enc = OneHotEncoder(handle_unknown='ignore')

X_train_enc = enc.fit_transform(X=X_train)
X_test_enc = enc.transform(X=X_test)

# train_data = tf.data.Dataset.from_tensor_slices((X_train_enc, y_train))
# train_data = train_data.repeat().shuffle(len(X_train_enc))
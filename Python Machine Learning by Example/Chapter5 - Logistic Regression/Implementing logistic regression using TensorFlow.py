import tensorflow as tf
import pandas as pd

# Read in the first 6000 rows.
df = pd.read_csv('train.csv', nrows=6000)
print(df)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)
print(X)

y = df['click']
print(y)

X_train = X[: 6000 * 0.9] # Use 90% of the read-in rows for training.
y_train = y[: 6000 * 0.9]

X_test = X[6000 * 0.9 :]
y_test = y[6000 * 0.9 :]
import pandas as pd

n_rows = 100000 * 11

df = pd.read_csv(filepath_or_buffer='train.csv', nrows=n_rows)

print(df)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)

print(X)

X_train = X.to_numpy()

print(X_train)

y = df['click']

print(y)

y_train = df['click'].to_numpy()

print(y_train)

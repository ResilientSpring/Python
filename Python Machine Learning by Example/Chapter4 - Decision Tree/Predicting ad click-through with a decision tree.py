import pandas as pd
from sklearn.preprocessing import OneHotEncoder

the_number_of_rows_to_read = 300000
dataset = pd.read_csv(filepath_or_buffer='train.csv', nrows=the_number_of_rows_to_read)

print(dataset.info())
print(dataset.head(50))
print(dataset.tail(50))
print(dataset.describe())

y = dataset.filter(['click'])

print(y)

X = dataset.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)

print(X)
print(X.shape)

the_number_of_training_samples = int(the_number_of_rows_to_read * 0.9)

X_train = X[:the_number_of_training_samples]
y_train = y[:the_number_of_training_samples]
X_test = X[the_number_of_training_samples:]
y_test = y[the_number_of_training_samples:]


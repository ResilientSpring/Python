import pandas as pd

the_number_of_rows_to_read = 30000
dataset = pd.read_csv(filepath_or_buffer='train.csv', nrows=the_number_of_rows_to_read)

print(dataset.head(5))

y = dataset.filter(['click'])

print(y)

X = dataset.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)

print(X)
print(X.shape)

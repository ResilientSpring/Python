import pandas as pd

the_number_of_rows_to_read = 30000
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

# So how long in total is the train.csv?
dataset2 = pd.read_csv('train.csv')
print(dataset2.info())
print(dataset2.tail(50))
print(dataset2.describe())

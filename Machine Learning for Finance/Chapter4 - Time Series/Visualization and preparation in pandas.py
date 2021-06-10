import pandas as pd

train = pd.read_csv('train_1.csv').fillna(0)
print(train.head())

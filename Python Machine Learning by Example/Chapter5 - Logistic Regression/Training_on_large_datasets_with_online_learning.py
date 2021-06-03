import pandas as pd

n_rows = 100000 * 11

df = pd.read_csv(filepath_or_buffer='train.csv', nrows=n_rows)

print(df)

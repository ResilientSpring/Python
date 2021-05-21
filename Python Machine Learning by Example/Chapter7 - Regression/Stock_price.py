import pandas as pd

my_data = pd.read_csv(filepath_or_buffer="20051201_20051210.csv", index_col="Date")

print(my_data)

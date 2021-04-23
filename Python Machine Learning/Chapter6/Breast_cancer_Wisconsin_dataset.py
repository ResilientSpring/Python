import pandas as pd

url = "https://raw.githubusercontent.com/rasbt/python-machine-learning-book-3rd-edition/master/ch06/wdbc.data"
df = pd.read_csv(filepath_or_buffer=url, header=None, index_col=False)
print(df)
import pandas as pd

url = "https://raw.githubusercontent.com/rasbt/python-machine-learning-book-3rd-edition/master/ch04/wine.data"
df = pd.read_csv(filepath_or_buffer=url, header=None)
print(df)
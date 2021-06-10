import pandas as pd

df = pd.read_csv('movie_data.csv', encoding='utf-8')
print(df.head(5))
print(df.shape)

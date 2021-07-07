import pandas as pd

df = pd.read_csv('year2018_public_research.csv', encoding='utf-8', header=0, skipinitialspace=True,
                 thousands=r',',)
print(df)

total = df['核定經費'].sum()
print(total)

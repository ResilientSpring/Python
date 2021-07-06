import pandas as pd

pd.options.plotting.backend = 'plotly'

url = 'https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv'
microsoft = pd.read_csv(url, parse_dates=['Date'], index_col=['Date'])
print(microsoft)
print(microsoft.info())
print(microsoft.describe())

microsoft = microsoft.sort_index()
print(microsoft)

rows_from2019 = microsoft.loc['2019', 'Adj Close']
print(rows_from2019)

# Plot the data between June 2019 and May 2020
rows2020_2019 = microsoft.loc['2019-06':'2020-05', 'Adj Close']
print(rows2020_2019)

rows2020_2019.plot()

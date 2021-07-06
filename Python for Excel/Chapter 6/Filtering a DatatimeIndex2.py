import pandas as pd

url = 'https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv'
microsoft = pd.read_csv(url, parse_dates=['Date'], index_col=['Date'])
print(microsoft)
print(microsoft.info())
print(microsoft.describe())

microsoft = microsoft.sort_index()
print(microsoft)

rows_from2019 = microsoft['2019', 'Adj Close']
print(rows_from2019)

import pandas as pd
import numpy as np

pd.options.plotting.backend = 'plotly'

daily_index = pd.date_range(start="2020-02-28", periods=4, freq='D')
print(daily_index)

flashback = pd.date_range(start='2021-07-05', freq='D', periods=10)
print(flashback)

# This creates a DatetimeIndex based on start/end timestamp.
# The frequency is set to 'weekly on Sundays'.
weekly_index = pd.date_range(start='2020-01-01', end='2020-01-31', freq='W-SUN')
print(weekly_index)

weekly_index2 = pd.date_range(start='2021-07-06', end='2021-08-31', freq='W-SUN')
print(weekly_index2)

# Construct a DataFrame based on the weekly_index.
# This could be the visitor count of a museum that only opens on Sundays.
count = pd.DataFrame(data=[21, 15, 33, 34], columns=['visitors'], index=weekly_index)
print(count)

msft = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv')
print(msft)
print(msft.info())

msft.loc[:, 'Date'] = pd.to_datetime(msft['Date'])
print(msft.dtypes)
print(msft)
print(msft.info())

print(30*'=')

microsoft = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                        index_col='Date', parse_dates=['Date'])
print(microsoft)
print(microsoft.info())

print(30*'=')

microsoft2 = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                         parse_dates=['Date'])
print(microsoft2)
print(microsoft2.info())
print(microsoft2.dtypes)

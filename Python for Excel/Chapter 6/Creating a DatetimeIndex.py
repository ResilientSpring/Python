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

# Make sure to assign the transformed column back to the original DataFrame
# if you want to change the original DataFrame:
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

print(30*'=')

# Column type conversion (method 1)
microsoft3 = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                         parse_dates=['Date'], dtype={"Volume": float})
print(microsoft3)
print(microsoft3.info())
print(microsoft3.dtypes)

print(30*'=')

# Column type conversion (method 2)
microsoft4 = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                         parse_dates=['Date'])
microsoft4.loc[:, 'Volume'] = microsoft4['Volume'].astype('float')
print(microsoft4['Volume'].dtype)

print(30*'=')

# My personal experiments
microsoft5 = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                         parse_dates=['Date'])
microsoft5['Volume'] = microsoft5['Volume'].astype('float')
print(microsoft5['Volume'].dtype)

print(30*'=')

# My personal experiments
microsoft6 = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                         parse_dates=['Date'])
microsoft6['Volume'].astype('float')
print(microsoft6['Volume'].dtype)

print(30*'=')

# My personal experiments
microsoft7 = pd.read_csv('https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv',
                         parse_dates=['Date'])
# microsoft7['Volume'].astype('float', inplace=True)
print(microsoft7['Volume'].dtype)

print(30*'=')

microsoft = microsoft.sort_index()
print(microsoft)

# If you need to access only parts of a DatetimeIndex, like the date part without the time,
# access the date attribute like this:
print(microsoft.index.date)

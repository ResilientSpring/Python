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

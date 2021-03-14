# Let's start by importing the packages we use in this chapter
# and by setting the plotting backend to Plotly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt;

pd.options.plotting.backend = "plotly";

# This create a DatetimeIndex based on a start timestamp,
# number of periods and frequency ("D" = daily).
daily_index = pd.date_range("2020-02-28", periods=4, freq="D");
print(daily_index);
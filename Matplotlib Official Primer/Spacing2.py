import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [6, 16, 75, 160, 244, 260, 145, 73, 16, 4, 1]

# In my original code I create a series and run on that,
# so for consistency I create a series from the list.
freq_series = pd.Series(frequencies)

x_labels = [108300.0, 110540.0, 112780.0, 115020.0, 117260.0, 119500.0,
            121740.0, 123980.0, 126220.0, 128460.0, 130700.0]


# dataframe using frequencies and x_labels from the OP
df = pd.DataFrame({'Frequency': frequencies}, index=x_labels)

# plot
ax = df.plot(kind='bar', figsize=(12, 8), title='Amount Frequency',
             xlabel='Amount ($)', ylabel='Frequency', legend=False)

# annotate
ax.bar_label(ax.containers[0], label_type='edge')

# pad the spacing between the number and the edge of the figure
ax.margins(y=0.6)

plt.show()

# Source: https://stackoverflow.com/a/67561982/14900011

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

month_as_of_now = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

deaths = [[14, 30, 18, 28, 31, 31], # Jan
          [23, 55, 38, 46, 62, 70], # Feb
          [36, 70, 56, 82, 83, 98], # Mar
          [47, 85, 77, 106, 106, 123], # Apr
          [57, 106, 99, 128, 147, 153], # May
          [66, 123, 123, 151, 172, 177], # Jun
          [73, 146, 145, 178, 190, 193], # Jul
          ]

df = pd.DataFrame(data=deaths,
                  index=month_as_of_now,
                  columns=administrative_duty)
print(df)

# Get some pastel shades for the colors
colors = plt.colormaps().BuPu(np.linspace(0, 0.5, len(month_as_of_now)))
n_rows = len(deaths)

index = np.arange(len(administrative_duty)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(administrative_duty))

# Plot bars and create text labels for the table
cell_text = []

plt.show()

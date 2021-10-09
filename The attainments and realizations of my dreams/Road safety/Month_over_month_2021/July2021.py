import matplotlib.pyplot as plt
import pandas as pd

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

month_as_of_now = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

deaths = [[14, 30, 18, 28, 31, 31], # Jan
          [23, 55, 38, 46, 62, 70], # Feb
          [36, 70, 56, 82, 83, 98], # Mar
          [47, 85, 77, 106, 106, 123], # Apr
          [57, 106, 99, 128, 147, 153], # May
          [66, 123, 123, 151, 172, 177], # Jun
          [73, 146, 145, 178, 190, 173], # Jul
          ]

df = pd.DataFrame(data=deaths,
                  index=month_as_of_now,
                  columns=administrative_duty)
print(df)

figure, axes = plt.subplots()

axes.plot(month_as_of_now, df.loc[:, "Taipei"].to_numpy(), label="Taipei")
axes.plot(month_as_of_now, df.loc[:, "New Taipei"].to_numpy(), label="New Taipei")
axes.plot(month_as_of_now, df.loc[:, "Taoyuan"].to_numpy(), label="Taoyuan")
axes.plot(month_as_of_now, df.loc[:, "Taichung"].to_numpy(), label="Taichung")
axes.plot(month_as_of_now, df.loc[:, "Tainan"].to_numpy(), label="Tainan")
axes.plot(month_as_of_now, df.loc[:, "Kaohsiung"].to_numpy(), label="Kaohsiung")

axes.legend()

axes.grid(True)

plt.show()

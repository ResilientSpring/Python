import matplotlib.pyplot as plt
import pandas as pd

importation = pd.read_csv("2020_import_value_from_each_customs.csv", header=0, index_col=0)

print(importation)

percentile = [(1895203688 / 9632849116),
              (4734911841 / 9632849116),
              (1317064881 / 9632849116),
              (1685668707 / 9632849116)]

print(percentile)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Keelung customs\n(Container ports in N.TW & E.TW)', 'Taipei customs\n(Airports in N.TW,\n ' \
                                                              'including Miaoli county )', \
         'Taichung customs\n(Airport & container\n ports in C.TW,\n incl. Yunlin county)', \
         'Kaohsiung customs\n(Airport & container ports\n in S.TW)'

sizes = [19.67, 49.15, 13.67, 17.49]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("The contribution of each region to total import ($NTD) in Taiwan 2020")

textstr = 'Dataset:https://portal.sw.nat.gov.tw/APGA/GA11_LIST'

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax1.text(0.09, 0.00, textstr, transform=ax1.transAxes, fontsize=11,
         verticalalignment='top', bbox=props)

plt.show()

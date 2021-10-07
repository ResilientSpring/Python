import pandas as pd
import matplotlib.pyplot as plt

exportation = pd.read_csv("2020_export_value_from_each_customs.csv", header=0, index_col=0)

print(exportation)

percentile = [(1544101314 / 13800075242),
              (6674773304 / 13800075242),
              (2550413664 / 13800075242),
              (3030786960 / 13800075242),
              100]

print(percentile)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Keelung customs\n(Container ports in N.TW & E.TW)', 'Taipei customs\n(Airports in N.TW,\n ' \
                                                              'including Miaoli county )', \
         'Taichung customs\n(Airport & container\n ports in C.TW,\n incl. Yunlin county)', \
         'Kaohsiung customs\n(Airport & container ports\n in S.TW)'

sizes = [11.18, 48.36, 18.48, 21.96]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90,
        textprops=dict(color="w"))

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("The contribution of each region to total export ($NTD) in Taiwan 2020")

textstr = '\n'.join((
    r'Dataset:',
    r'https://portal.sw.nat.gov.tw/APGA/GA11_LIST',
))
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax1.text(0.09, 0.01, textstr, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

plt.show()

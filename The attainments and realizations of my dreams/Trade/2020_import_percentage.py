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



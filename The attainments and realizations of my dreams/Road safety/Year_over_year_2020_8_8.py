import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colour
import matplotlib.patheffects as path_effects

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

year = ["2009", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "2020"]

death = [[133, 254, 198, 318, 340, 402],  # 2009
         [152, 255, 227, 373, 319, 388],  # 2010
         [140, 264, 195, 382, 346, 373],  # 2011
         [130, 252, 195, 370, 288, 417],  # 2012
         [140, 223, 191, 308, 311, 375],  # 2013
         [138, 219, 221, 302, 290, 387],  # 2014
         [137, 212, 203, 275, 289, 364],  # 2015
         [157, 266, 203, 259, 269, 329],  # 2016
         [106, 256, 213, 217, 246, 289],  # 2017
         [137, 248, 244, 245, 289, 280],  # 2018
         [131, 225, 249, 270, 294, 351],  # 2019
         [102, 232, 264, 325, 317, 347],  # 2020
         #         [73, 146, 145, 178, 190, 193],  # 2021/01-07
         ]

df = pd.DataFrame(data=death, columns=administrative_duty, index=year)

print(df)

Taipei = df.loc[:, "Taipei"].to_numpy()

print(Taipei)

New_Taipei = df.loc[:, "New Taipei"].to_numpy()
Taoyuan = df.loc[:, "Taoyuan"].to_numpy()
Taichung = df.loc[:, "Taichung"].to_numpy()
Tainan = df.loc[:, "Tainan"].to_numpy()
Kaohsiung = df.loc[:, "Kaohsiung"].to_numpy()

summary = [df["Taipei"].sum(), df["New Taipei"].sum(), df["Taoyuan"].sum(), df["Taichung"].sum(),
           df["Tainan"].sum(), df["Kaohsiung"].sum()]

print(summary)

cumulative_sum = pd.DataFrame(data=summary,
                              columns=["Cumulative Deaths (2009-2020)"],
                              index=administrative_duty)

print(cumulative_sum)

figure, (axes1, axes2) = plt.subplots(2)

axes1.plot(year, Taipei, label="Taipei")
axes1.plot(year, New_Taipei, label="New Taipei")
axes1.plot(year, Taoyuan, label="Taoyuan")
axes1.plot(year, Taichung, label="Taichung")
axes1.plot(year, Tainan, label="Tainan")
axes1.plot(year, Kaohsiung, label="Kaohsiung")

axes1.set_title("The Number of Deaths in Road Accident in Taiwan by Region")
axes1.set_xlabel("Year")
axes1.set_ylabel("The number of deaths")

axes1.legend()

axes1.grid(True)

# hide axes
# axes[0, 1].patch.set_visible(False)
axes2.axis('off')
axes2.axis('tight')

axes2.table(cellText=cumulative_sum.values,
            colLabels=cumulative_sum.columns,
            colColours=[colour.CSS4_COLORS.get('springgreen')],
            colWidths=[0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
            cellColours=['w', 'w', 'w', 'w', 'w', 'w'],
            cellLoc='center',
            rowLabels=cumulative_sum.index,
            rowColours=[colour.CSS4_COLORS.get('lightskyblue'),
                        colour.CSS4_COLORS.get('lightskyblue'),
                        colour.CSS4_COLORS.get('lightskyblue'),
                        colour.CSS4_COLORS.get('lightskyblue'),
                        colour.CSS4_COLORS.get('lightskyblue'),
                        colour.CSS4_COLORS.get('lightskyblue')],
            loc='center',
            url='Reference:\nhttps://roadsafety.tw/Dashboard/Custom?type=30日死亡人數'
            )


figure.tight_layout()

# matplotlib text [1][2]
text = figure.text(0.5, 0.02,
                   'Reference:https://roadsafety.tw/Dashboard/Custom?type=30日死亡人數',
                   horizontalalignment='center',
                   verticalalignment='center',
                   size=13,
                   fontproperties='MS Gothic')

text.set_path_effects([path_effects.Normal()])

plt.show()

# References:
# 1. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
# 2. https://matplotlib.org/stable/tutorials/advanced/patheffects_guide.html#sphx-glr-tutorials-advanced-patheffects-guide-py


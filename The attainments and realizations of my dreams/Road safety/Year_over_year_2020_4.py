import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colour

administrative_duty = ["Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan", "Kaohsiung"]

year = ["2009", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "2020"]

death = [[133, 254, 198, 318, 340, 402], # 2009
         [152, 255, 227, 373, 319, 388], # 2010
         [140, 264, 195, 382, 346, 373], # 2011
         [130, 252, 195, 370, 288, 417], # 2012
         [140, 223, 191, 308, 311, 375], # 2013
         [138, 219, 221, 302, 290, 387], # 2014
         [137, 212, 203, 275, 289, 364], # 2015
         [157, 266, 203, 259, 269, 329], # 2016
         [106, 256, 213, 217, 246, 289], # 2017
         [137, 248, 244, 245, 289, 280], # 2018
         [131, 225, 249, 270, 294, 351], # 2019
         [102, 232, 264, 325, 317, 347], # 2020
         #         [73, 146, 145, 178, 190, 193],  # 2021/01-07
         ]

df = pd.DataFrame(data=death, columns=administrative_duty, index=year)

print(df)

summary = [df["Taipei"].sum(), df["New Taipei"].sum(), df["Taoyuan"].sum(), df["Taichung"].sum(),
           df["Tainan"].sum(), df["Kaohsiung"].sum()]

print(summary)

cumulative_sum = pd.DataFrame(data=summary,
                              columns=["Cumulative sum"],
                              index=administrative_duty)

print(cumulative_sum)

figure, axes = plt.subplots()

# hide axes [1]
figure.patch.set_visible(False)
axes.axis('off')
axes.axis('tight')

# Plot a table using matplotlib.[2]
axes.table(cellText=cumulative_sum.values,
           colLabels=cumulative_sum.columns,
           colColours=[colour.CSS4_COLORS.get('springgreen')],
           colWidths=[0.4, 0.4, 0.4, 0.4, 0.4, 0.4], # colwidths matplotlib [3][4]
           cellColours=['w', 'w', 'w', 'w', 'w', 'w'],
           cellLoc='center',
           rowLabels=cumulative_sum.index,
           rowColours=[colour.CSS4_COLORS.get('lightskyblue'), #[5][6][7]
                       colour.CSS4_COLORS.get('lightskyblue'),
                       colour.CSS4_COLORS.get('lightskyblue'),
                       colour.CSS4_COLORS.get('lightskyblue'),
                       colour.CSS4_COLORS.get('lightskyblue'),
                       colour.CSS4_COLORS.get('lightskyblue')],
           loc='center',
           )

figure.tight_layout()

plt.show()

# References:
# 1. https://stackoverflow.com/a/45936469
# 2. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html
# 3. https://stackoverflow.com/a/46977181
# 4. https://stackoverflow.com/a/15514091
# 5. https://matplotlib.org/stable/gallery/color/named_colors.html
# 6. https://stackoverflow.com/a/46664216
# 7. https://matplotlib.org/stable/gallery/color/color_demo.html

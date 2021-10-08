import pandas as pd
import matplotlib.pyplot as plt

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

df.plot(grid=True, use_index=True, figsize=(10, 8),
        title="The Number of Deaths in Road Accident in Taiwan by Region")

plt.xlabel("Year")
plt.ylabel("The number of deaths (Unit: person)")
plt.text(x=1, y=1, s="Reference:\nhttps://roadsafety.tw/Dashboard/Custom?type=30日死亡人數",
         style='italic', bbox={'facecolor': 'red', 'alpha': 0.8, 'pad': 10}, fontproperties="MS Gothic")

plt.show()

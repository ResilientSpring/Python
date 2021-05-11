import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

df = pd.DataFrame(data=[
    [1, "國立臺灣大學", 237370, "North"],
    [2, "國立成功大學", 141139, "South"],
    [3, "國立清華大學", 122096, "North"],
    [4, "國立陽明交通大學（交大校區）", 105386, "North"],
    [5, "國立中興大學", 43431, "North"],
    [6, "國立中央大學", 43086, "North"],
    [7, "國立陽明交通大學（陽明校區）", 34354, "North"],
    [8, "國立政治大學", 32993, "North"],
    [9, "國立中山大學", 32298, "South"],
    [10, "國立臺灣師範大學", 22792, "North"],
    [11, "國立中正大學", 15636, "South"],
    [12, "國立臺灣海洋大學", 14558, "North"],
    [13, "國立臺北大學", 8791, "North"],
    [14, "國立暨南國際大學", 7940, "North"],
    [15, "國立彰化師範大學", 7442, "North"],
    [16, "國立東華大學", 7071],
    [17, "國立嘉義大學", 6718, "South"],
    [18, "國立宜蘭大學", 6651, "North"],
    [19, "國立屏東大學", 6616, "South"],
    [20, "國立臺東大學", 6239],
    [21, "國立臺灣藝術大學", 5915, "North"],
    [22, "國立臺北教育大學", 5548, "North"],
    [23, "國立高雄大學", 5495, "South"],
    [24, "國立臺北藝術大學", 5469, "North"],
    [25, "國立臺中教育大學", 5447, "North"],
    [26, "國立臺南大學", 5100, "South"],
    [27, "臺北市立大學", 5054, "North"],
    [28, "國立體育大學", 4795, "North"],
    [29, "國立聯合大學", 4561, "North"],
    [30, "國立高雄師範大學", 4408, "South"],
    [31, "國立臺灣體育運動大學", 3226, "North"],
    [32, "國立金門大學", 3171],
    [33, "國立臺灣體育運動大學", 3226],
    [34, "國立臺南藝術大學", 2046, "South"],

    [1, "國立高雄科技大學", 39491, "South"],
    [2, "國立臺灣科技大學", 33344, "North"],
    [3, "國立臺北科技大學", 29535, "North"],
    [4, "國立虎尾科技大學", 24529, "South"],
    [5, "國立雲林科技大學", 21800, "South"],
    [6, "國立屏東科技大學", 16629, "South"],
    [7, "國立勤益科技大學", 13979, "North"],
    [8, "國立臺北護理健康大學", 8600, "North"],
    [9, "國立高雄餐旅大學", 7929, "South"],
    [10, "國立臺北商業大學", 4774, "North"],
    [11, "國立臺東專科學校", 4119],
    [12, "國立臺中科技大學", 3511, "North"],
    [13, "國立臺灣戲曲學院", 2989, "North"],
    [14, "國立澎湖科技大學", 2824],
    [15, "國立臺南護理專科學校", 1922, "South"]
])

print(df)

df2 = df.copy()
print(df2)

df2.columns = ["Number", "Name", "Budget", "Region"]  # Rename the columns [1]
print(df2)

class_le = LabelEncoder()

y = class_le.fit_transform(y=df2["Region"].values)
print(y)

df2["Region_encoding"] = y

print(df2)

df3 = pd.DataFrame(index=["Northern Taiwan", "Southern Taiwan"], columns=["Budget"],
                   data=[df2.query("Region_encoding == 0")["Budget"].sum(),  # [1]
                         df2.query("Region_encoding == 1")["Budget"].sum()])
print(df3)

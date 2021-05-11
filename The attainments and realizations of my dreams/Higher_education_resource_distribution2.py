import numpy as np
import pandas as pd

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
    [34, "國立臺南藝術大學", 2046, "South"]
])

print(df)

df2 = pd.DataFrame(index=["Northern Taiwan", "Southern Taiwan"], columns=["Budget"],
                   data=[df.iloc[df.iloc[:, 3] == "North", df.iloc[:, 2]].sum(axis=0),
                         df.iloc[df.iloc[:, 3] == "South", df.iloc[:, 2]].sum(axis=0)])

print(df2)

df3 = pd.DataFrame(index=["Northern Taiwan", "Southern Taiwan"], columns=["Budget"],
                   data=[df.iloc[df.iloc[:, 3] == "North", df.iloc[:, 2]].sum(),
                         df.iloc[df.iloc[:, 3] == "South", df.iloc[:, 2]].sum()])

# Reference:
# https://stackoverflow.com/questions/37947641/pandas-how-to-sum-columns-based-on-conditional-of-other-column-values
# https://stackoverflow.com/questions/28236305/how-do-i-sum-values-in-a-column-that-match-a-given-condition-using-pandas
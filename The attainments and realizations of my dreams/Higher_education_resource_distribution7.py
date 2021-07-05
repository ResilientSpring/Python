import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

df = pd.DataFrame(data=[
    [1, "國立臺灣大學", "National Taiwan University", 237370, "North", ],
    [2, "國立成功大學", "National Cheng Kung University", 141139, "South", ],
    [3, "國立清華大學", "National Tsing Hua University", 122096, "North", "Derived from Beijing, China's Tsing Hua University"],
    [4, "國立陽明交通大學（交大校區）", "National Yang Ming Chiao Tung University (Hsinchu)", 105386, "North", "Derived from Shanghai, China's ChiaoTung University"],
    [5, "國立中興大學", "National Chung Hsing University", 43431, "North", ],
    [6, "國立中央大學", "National Central University", 43086, "North", ],
    [7, "國立陽明交通大學（陽明校區）", "National Yang Ming Chiao Tung University (Taipei)", 34354, "North", ],
    [8, "國立政治大學", "National Chengchi University", 32993, "North", "Literally, 'National Politics University'"],
    [9, "國立中山大學", "National Sun Yat-sen University", 32298, "South", ],
    [10, "國立臺灣師範大學", "National Taiwan Normal University", 22792, "North", ],
    [11, "國立中正大學", "National Chung Cheng University", 15636, "South", "Literally, National Chiang Chung-cheng University"],
    [12, "國立臺灣海洋大學", "National Taiwan Ocean University", 14558, "North", ],
    [13, "國立臺北大學", "National Taipei University", 8791, "North", ],
    [14, "國立暨南國際大學", "National Chi Nan University", 7940, "North", ],
    [15, "國立彰化師範大學", "National Changhua University of Education", 7442, "North", ],
    [16, "國立東華大學", "National Dong Hwa University", 7071, "Hualien County", ],
    [17, "國立嘉義大學", "National Chiayi University", 6718, "South", ],
    [18, "國立宜蘭大學", "National Ilan University", 6651, "North", ],
    [19, "國立屏東大學", "National Pingtung University", 6616, "South", ],
    [20, "國立臺東大學", "National Taitung University", 6239, "Taitung County", ],
    [21, "國立臺灣藝術大學", "National Taiwan University of Arts", 5915, "North", ],
    [22, "國立臺北教育大學", "National Taipei University of Education", 5548, "North", ],
    [23, "國立高雄大學", "National University of Kaohsiung", 5495, "South", ],
    [24, "國立臺北藝術大學", "The Taipei National University of the Arts", 5469, "North", ],
    [25, "國立臺中教育大學", "National Taichung University of Education", 5447, "North", ],
    [26, "國立臺南大學", "National University of Tainan", 5100, "South", ],
    [27, "臺北市立大學", "University of Taipei", 5054, "North", ],
    [28, "國立體育大學", "National Taiwan Sport University", 4795, "North", ],
    [29, "國立聯合大學", "National United University", 4561, "North", ],
    [30, "國立高雄師範大學", "National Kaohsiung Normal University", 4408, "South", ],
    [31, "國立臺灣體育運動大學", "National Taiwan University of Sport", 3226, "North", ],
    [32, "國立金門大學", "National Quemoy University", 3171, ],
    [33, "國立臺灣體育運動大學", "National Taiwan University of Sport", 3226, "North", ],
    [34, "國立臺南藝術大學", "Tainan National University of the Arts", 2046, "South", ],

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
    [15, "國立臺南護理專科學校", 1922, "South"],

    [1, "臺北醫學大學", 26919, "North"],
    [2, "中國醫藥大學", 19722, "North"],
    [3, "長庚大學", 16186, "North"],
    [4, "中原大學", 14880, "North"],
    [5, "高雄醫學大學", 14461, "South"],
    [6, "逢甲大學", 14313, "North"],
    [7, "東海大學", 11731, "North"],
    [8, "元智大學", 10559, "North"],
    [9, "義守大學", 9587, "South"],
    [10, "東吳大學", 9579, "North"],
    [11, "輔仁大學", 9560, "North"],
    [12, "靜宜大學", 9523, "North"],
    [13, "淡江大學", 8965, "North"],
    [14, "銘傳大學", 7327, "North"],
    [15, "中國文化大學", 6772, "North"],
    [16, "實踐大學", 6541, "North"],
    [17, "亞洲大學", 6337, "North"],
    [18, "大葉大學", 6153, "North"],
    [19, "世新大學", 6104, "North"],
    [20, "中山醫學大學", 6056, "North"],
    [21, "長榮大學", 5897, "South"],
    [22, "南華大學", 5837, "South"],
    [23, "慈濟大學", 5810],
    [24, "中華大學", 5209, "North"],
    [25, "大同大學", 4515, "North"],
    [26, "佛光大學", 4419, "North"],
    [27, "馬偕醫學院", 3727, "North"],
    [28, "華梵大學", 2952, "North"],
    [29, "玄奘大學", 2806, "North"],
    [30, "中信金融管理學院", 1976, "South"],
    [31, "開南大學", 1711, "North"],
    [32, "真理大學", 1624, "North"],
    [33, "台灣首府大學", 779, "South"],
    [34, "明道大學", 328, "North"],
    [35, "康寧大學", 256, "North"],
    [36, "一貫道天皇學院", 155, "South"],
    [37, "法鼓文理學院", 154, "North"],

    [1, "崑山科技大學", 21080, "South"],
    [2, "正修科技大學", 19506, "South"],
    [3, "南臺科技大學", 16357, "South"],
    [4, "龍華科技大學", 12662, "North"],
    [5, "弘光科技大學", 11847, "North"],
    [6, "明志科技大學", 10031, "North"],
    [7, "嘉南藥理大學", 9020, "South"],
    [8, "樹德科技大學", 8040, "South"],
    [9, "致理科技大學", 7911, "North"],
    [10, "遠東科技大學", 7834, "South"],
    [11, "朝陽科技大學", 7646, "North"],
    [12, "中國科技大學", 7360, "North"],
    [13, "醒吾科技大學", 6895, "North"],
    [14, "長庚科技大學", 6288, "North"],
    [15, "文藻外語大學", 6212, "South"],
    [16, "嶺東科技大學", 5603, "North"],
    [17, "修平科技大學", 5421, "North"],
    [18, "明新科技大學", 5401, "North"],
    [19, "中華醫事科技大學", 5395, "South"],
    [20, "中臺科技大學", 5179, "North"],
    [21, "健行科技大學", 5169, "North"],
    [22, "景文科技大學", 5022, "North"],
    [23, "慈濟科技大學", 4853],
    [24, "德明財經科技大學", 4498, "North"],
    [25, "輔英科技大學", 4382, "South"],
    [26, "大仁科技大學", 4251, "South"],
    [27, "台南應用科技大學", 4218, "South"],
    [28, "美和科技大學", 3864, "South"],
    [29, "南開科技大學", 3506, "North"],
    [30, "吳鳳科技大學", 3468, "South"],
    [31, "耕莘健康管理專科學校", 3415, "North"],
    [32, "元培醫事科技大學", 3176, "North"],
    [33, "中華科技大學", 3068, "North"],
    [34, "華夏科技大學", 2965, "North"],
    [35, "樹人醫護管理專科學校", 2964, "South"],
    [36, "臺北城市科技大學", 2763, "North"],
    [37, "亞東技術學院", 2702, "North"],
    [38, "僑光科技大學", 2626, "North"],
    [39, "仁德醫護管理專科學校", 2598, "North"],
    [40, "萬能科技大學", 2575, "North"],
    [41, "台北海洋科技大學", 2398, "North"],
    [42, "馬偕醫護管理專科學校", 2330, "North"],
    [43, "東南科技大學", 2296, "North"],
    [44, "宏國德霖科技大學", 2239, "North"],
    [45, "新生醫護管理專科學校", 2125, "North"],
    [46, "慈惠醫護管理專科學校", 2095],
    [47, "高苑科技大學", 1968, "South"],
    [48, "黎明技術學院", 1890, "North"],
    [49, "聖約翰科技大學", 1670, "North"],
    [50, "崇仁醫護管理專科學校", 1656, "South"],
    [51, "敏惠醫護管理專科學校", 1557, "South"],
    [52, "中州科技大學", 1420, "North"],
    [53, "南亞技術學院", 1375, "North"],
    [54, "崇右影藝科技大學", 1226, "North"],
    [55, "東方設計大學", 1162, "South"],
    [56, "育達科技大學", 1136, "North"],
    [57, "聖母醫護管理專科學校", 1118, "North"],
    [58, "經國管理暨健康學院", 1090, "North"],
    [59, "育英醫護管理專科學校", 994, "South"],
    [60, "大漢技術學院", 980],
    [61, "建國科技大學", 953, "North"],
    [62, "大同技術學院", 828, "South"],
    [63, "大華科技大學", 640, "North"],
    [64, "環球科技大學", 486, "South"],
    [65, "蘭陽技術學院", 447, "North"]
])

print(df)

df2 = df.copy()
print(df2)

df2.columns = ["Number", "Name", "English name", "Budget", "Region", "Note"]  # Rename the columns [1]
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

print(df3.plot())

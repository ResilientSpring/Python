import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

public_research_centric_university = pd.DataFrame(data=[
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
])

public_vocational_centric_university = pd.DataFrame(data=[
    [1, "國立高雄科技大學", "National Kaohsiung University of Science and Technology", 39491, "South"],
    [2, "國立臺灣科技大學", "National Taiwan University of Science and Technology", 33344, "North"],
    [3, "國立臺北科技大學", "National Taipei University of Technology", 29535, "North"],
    [4, "國立虎尾科技大學", "National Formosa University", 24529, "South"],
    [5, "國立雲林科技大學", "National Yunlin University of Science and Technology ", 21800, "South"],
    [6, "國立屏東科技大學", "National Pingtung University of Science and Technology", 16629, "South"],
    [7, "國立勤益科技大學", "National Chin-Yi University of Technology ", 13979, "North"],
    [8, "國立臺北護理健康大學", "National Taipei University of Nursing and Health Sciences", 8600, "North"],
    [9, "國立高雄餐旅大學", "National Kaohsiung University of Hospitality and Tourism", 7929, "South"],
    [10, "國立臺北商業大學", "National Taipei University of Business", 4774, "North"],
    [11, "國立臺東專科學校", "National Taitung Junior College", 4119],
    [12, "國立臺中科技大學", "National Taichung University of Science and Technology", 3511, "North"],
    [13, "國立臺灣戲曲學院", "National Taiwan College of Performing Arts", 2989, "North"],
    [14, "國立澎湖科技大學", "National Penghu University of Science and Technology", 2824],
    [15, "國立臺南護理專科學校", "National Tainan Junior College of Nursing", 1922, "South"],
])

private_research_centric_university = pd.DataFrame(data=[
    [1, "臺北醫學大學", "Taipei Medical University", 26919, "North"],
    [2, "中國醫藥大學", "China Medical University", 19722, "North"],
    [3, "長庚大學", "Chang Gung University", 16186, "North"],
    [4, "中原大學", "Chung Yuan Christian University", 14880, "North"],
    [5, "高雄醫學大學", "Kaohsiung Medical University", 14461, "South"],
    [6, "逢甲大學", "Feng Chia University", 14313, "North"],
    [7, "東海大學", "Tunghai University", 11731, "North"],
    [8, "元智大學", "Yuan Ze University", 10559, "North"],
    [9, "義守大學", "I-SHOU University", 9587, "South"],
    [10, "東吳大學", "Soochow University", 9579, "North"],
    [11, "輔仁大學", "Fu Jen Catholic University", 9560, "North"],
    [12, "靜宜大學", "Providence University", 9523, "North"],
    [13, "淡江大學", "Tamkang University", 8965, "North"],
    [14, "銘傳大學", "Ming Chuan University", 7327, "North"],
    [15, "中國文化大學", "Chinese Culture University", 6772, "North"],
    [16, "實踐大學", "Shih Chien University", 6541, "North"],
    [17, "亞洲大學", "Asia University", 6337, "North"],
    [18, "大葉大學", "Dayeh University", 6153, "North"],
    [19, "世新大學", "Shih Hsin University", 6104, "North"],
    [20, "中山醫學大學", "Chung Shan Medical University", 6056, "North"],
    [21, "長榮大學", "Chang Jung Christian University", 5897, "South"],
    [22, "南華大學", "Nanhua University", 5837, "South"],
    [23, "慈濟大學", "Tzu Chi University", 5810],
    [24, "中華大學", "Chung Hua University", 5209, "North"],
    [25, "大同大學", "Tatung University", 4515, "North"],
    [26, "佛光大學", "Fo Guang University", 4419, "North"],
    [27, "馬偕醫學院", "Mackay Medical College", 3727, "North"],
    [28, "華梵大學", "Huafan University", 2952, "North"],
    [29, "玄奘大學", "Hsuan Chuang University", 2806, "North"],
    [30, "中信金融管理學院", "CTBC BUSINESS SCHOOL", 1976, "South"],
    [31, "開南大學", "Kainan University", 1711, "North"],
    [32, "真理大學", "Aletheia University", 1624, "North"],
    [33, "台灣首府大學", "Taiwan Shoufu University", 779, "South"],
    [34, "明道大學", "MingDao University", 328, "North"],
    [35, "康寧大學", "University of Kang Ning", 256, "North"],
    [36, "一貫道天皇學院", "I-Kuan Tao College", 155, "South"],
    [37, "法鼓文理學院", "Dharma Drum Institute of Liberal Arts", 154, "North"],
])

private_vocational_centric_university = pd.DataFrame(data=[
    [1, "崑山科技大學", "Kun Shan University", 21080, "South"],
    [2, "正修科技大學", "Cheng Shiu University", 19506, "South"],
    [3, "南臺科技大學", "Southern Taiwan University of Science and Technology", 16357, "South"],
    [4, "龍華科技大學", "Lunghwa University of Science and Technology", 12662, "North"],
    [5, "弘光科技大學", "Hungkuang University", 11847, "North"],
    [6, "明志科技大學", "Ming Chi University of Technology", 10031, "North"],
    [7, "嘉南藥理大學", "Chia Nan University of Pharmacy and Science", 9020, "South"],
    [8, "樹德科技大學", "Shu-Te University", 8040, "South"],
    [9, "致理科技大學", "Chihlee University of Technology", 7911, "North"],
    [10, "遠東科技大學", "Far East University", 7834, "South"],
    [11, "朝陽科技大學", "Chaoyang University of Technology", 7646, "North"],
    [12, "中國科技大學", "China University of Technology", 7360, "North"],
    [13, "醒吾科技大學", "Hsing Wu University", 6895, "North"],
    [14, "長庚科技大學", "Chang Gung University of Science and Technology", 6288, "North"],
    [15, "文藻外語大學", "Wenzao Ursuline University of Languages", 6212, "South"],
    [16, "嶺東科技大學", "Ling Tung University", 5603, "North"],
    [17, "修平科技大學", "Hsiuping University of Science and Technology", 5421, "North"],
    [18, "明新科技大學", "Minghsin University of Science and Technology", 5401, "North"],
    [19, "中華醫事科技大學", "Chung Hwa University of Medical Technology", 5395, "South"],
    [20, "中臺科技大學", "Central Taiwan University of Science and Technology", 5179, "North"],
    [21, "健行科技大學", "Chien Hsin University of Science and Technology", 5169, "North"],
    [22, "景文科技大學", "Jinwen University of Science and Technology", 5022, "North"],
    [23, "慈濟科技大學", "Tzu Chi University of Science and Technology", 4853],
    [24, "德明財經科技大學", "Takming University of Science and Technology", 4498, "North"],
    [25, "輔英科技大學", "Fooyin University", 4382, "South"],
    [26, "大仁科技大學", "Tajen University", 4251, "South"],
    [27, "台南應用科技大學", "Tainan University of Technology", 4218, "South"],
    [28, "美和科技大學", "Meiho University", 3864, "South"],
    [29, "南開科技大學", "Nan Kai University of Technology", 3506, "North"],
    [30, "吳鳳科技大學", "Wufeng University", 3468, "South"],
    [31, "耕莘健康管理專科學校", "Cardinal Tien Junior College of Healthcare and Management", 3415, "North"],
    [32, "元培醫事科技大學", "Yuanpei University of Medical Technology", 3176, "North"],
    [33, "中華科技大學", "China University of Science and Technology", 3068, "North"],
    [34, "華夏科技大學", "Hwa Hsia University of Technology", 2965, "North"],
    [35, "樹人醫護管理專科學校", "Shu-Zen Junior College of Medicine and Management", 2964, "South"],
    [36, "臺北城市科技大學", "Taipei City University of Science and Technology", 2763, "North"],
    [37, "亞東技術學院", "Oriental Institute of Technology", 2702, "North"],
    [38, "僑光科技大學", "Overseas Chinese University", 2626, "North"],
    [39, "仁德醫護管理專科學校", "Jen-Teh Junior College of Medicine, Nursing and Management", 2598, "North"],
    [40, "萬能科技大學", "Vanung University", 2575, "North"],
    [41, "台北海洋科技大學", "Taipei University of Marine Technology", 2398, "North"],
    [42, "馬偕醫護管理專科學校", "Mackay Junior College of Medicine, Nursing and Management", 2330, "North"],
    [43, "東南科技大學", "Tungnan University", 2296, "North"],
    [44, "宏國德霖科技大學", "Hungkuo Delin University of Technology", 2239, "North"],
    [45, "新生醫護管理專科學校", "Hsin Sheng Junior College of Medical Care and Management", 2125, "North"],
    [46, "慈惠醫護管理專科學校", "Tzu Hui Institute of Technology", 2095],
    [47, "高苑科技大學", "Kao Yuan University", 1968, "South"],
    [48, "黎明技術學院", "Lee-Ming Institute of Technology", 1890, "North"],
    [49, "聖約翰科技大學", "St. John's University", 1670, "North"],
    [50, "崇仁醫護管理專科學校", "Chung Jen Junior College of Nursing, Health Science and Management", 1656, "South"],
    [51, "敏惠醫護管理專科學校", "Min-Hwei College of Health Care Management", 1557, "South"],
    [52, "中州科技大學", "Chung Chou University of Science and Technology", 1420, "North"],
    [53, "南亞技術學院", "Nanya Institute of Technology", 1375, "North"],
    [54, "崇右影藝科技大學", "Chungyu University of Film and Arts", 1226, "North"],
    [55, "東方設計大學", "Tung Fang Design University", 1162, "South"],
    [56, "育達科技大學", "Yu Da University of Science and Technology", 1136, "North"],
    [57, "聖母醫護管理專科學校", "St. Mary's Medicine Nursing and Management College", 1118, "North"],
    [58, "經國管理暨健康學院", "Ching Kuo Institute of Management and Health", 1090, "North"],
    [59, "育英醫護管理專科學校", "Yuh-Ing Junior College of Health Care and Management", 994, "South"],
    [60, "大漢技術學院", "Dahan Institute of Technology", 980],
    [61, "建國科技大學", "Chienkuo Technology University", 953, "North"],
    [62, "大同技術學院", "Tatung Institute of Technology", 828, "South"],
    [63, "大華科技大學", "Minth University of Science and Technology", 640, "North"],
    [64, "環球科技大學", "TransWorld University", 486, "South"],
    [65, "蘭陽技術學院", "Lan Yang Institute of Technology", 447, "North"]
])

print(public_research_centric_university)

header = ['Number', 'Chinese name', 'English name', 'Budget_received', 'Location', 'Note']

# Adding a header to National universities of R&D
public_research_centric_university.columns = header
print(public_research_centric_university)

# Filter the universities in the north.
condition = public_research_centric_university['Location'] == "North"
north_public_research = public_research_centric_university[condition]
print(north_public_research)

# Sum of the budget in the north.
total_north_public_research = north_public_research['Budget_received'].sum()
print(total_north_public_research)

# Filter the universities in the south.
condition = public_research_centric_university['Location'] == "South"
south_public_research = public_research_centric_university[condition]
print(south_public_research)

# Sum of the budget inn the south.
total_south_public_research = south_public_research['Budget_received'].sum()
print(total_south_public_research)

# The histogram of the data
plt.bar(['North', 'South'], [total_north_public_research, total_south_public_research])

plt.xlabel('Location (Northern Taiwan and Southern Taiwan)')
plt.ylabel('10 thousands New Taiwan Dollars')
plt.title(r'Government budget support for the universities in North vs South')

# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

plt.savefig('Total_difference.jpg')
plt.show()

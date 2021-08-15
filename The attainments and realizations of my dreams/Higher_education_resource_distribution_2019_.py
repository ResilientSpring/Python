import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
# Using the magic encoding
# -*- coding: utf-8 -*-


# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

public_research_centric_university = pd.DataFrame(data=[
    [1, "國立臺灣大學", "National Taiwan University", 225316, "North", ],
    [2, "國立成功大學", "National Cheng Kung University", 135161, "South", ],
    [3, "國立清華大學", "National Tsing Hua University", 115036, "North", "Derived from Beijing, China's Tsing Hua University"],
    [4, "國立陽明交通大學（交大校區）", "National Yang Ming Chiao Tung University (Hsinchu)", 105063, "North", "Derived from Shanghai, China's ChiaoTung University"],
    [5, "國立中興大學", "National Chung Hsing University", 40311, "North", ],
    [6, "國立中央大學", "National Central University", 41923, "North", ],
    [7, "國立陽明交通大學（陽明校區）", "National Yang Ming Chiao Tung University (Taipei)", 34016, "North", ],
    [8, "國立政治大學", "National Chengchi University", 33700, "North", "Literally, 'National Politics University'"],
    [9, "國立中山大學", "National Sun Yat-sen University", 30299, "South", ],
    [10, "國立臺灣師範大學", "National Taiwan Normal University", 22817, "North", ],
    [11, "國立中正大學", "National Chung Cheng University", 16441, "South", "Literally, National Chiang Chung-cheng University"],
    [12, "國立臺灣海洋大學", "National Taiwan Ocean University", 13389, "North", ],
    [13, "國立臺北大學", "National Taipei University", 7755, "North", ],
    [14, "國立暨南國際大學", "National Chi Nan University", 7204, "North", ],
    [15, "國立彰化師範大學", "National Changhua University of Education", 5924, "North", ],
    [16, "國立東華大學", "National Dong Hwa University", 5220, "Hualien County", ],
    [17, "國立嘉義大學", "National Chiayi University", 5765, "South", ],
    [18, "國立宜蘭大學", "National Ilan University", 5449, "North", ],
    [19, "國立屏東大學", "National Pingtung University", 6774, "South", ],
    [20, "國立臺東大學", "National Taitung University", 5129, "Taitung County", ],
    [21, "國立臺灣藝術大學", "National Taiwan University of Arts", 3188, "North", ],
    [22, "國立臺北教育大學", "National Taipei University of Education", 5339, "North", ],
    [23, "國立高雄大學", "National University of Kaohsiung", 4664, "South", ],
    [24, "國立臺北藝術大學", "The Taipei National University of the Arts", 4932, "North", ],
    [25, "國立臺中教育大學", "National Taichung University of Education", 5097, "North", ],
    [26, "國立臺南大學", "National University of Tainan", 4891, "South", ],
    [27, "臺北市立大學", "University of Taipei", 4440, "North", ],
    [28, "國立體育大學", "National Taiwan Sport University", 4088, "North", ],
    [29, "國立聯合大學", "National United University", 4603, "North", ],
    [30, "國立高雄師範大學", "National Kaohsiung Normal University", 4057, "South", ],
    [31, "國立臺灣體育運動大學", "National Taiwan University of Sport", 2919, "North", ],
    [32, "國立金門大學", "National Quemoy University", 3609, ],
    # [33, "國立臺灣體育運動大學", "National Taiwan University of Sport", 3226, "North", ],
    [33, "國立臺南藝術大學", "Tainan National University of the Arts", 1407, "South", ],
])

public_vocational_centric_university = pd.DataFrame(data=[
    [1, "國立高雄科技大學", "National Kaohsiung University of Science and Technology", (20123+14389+5422), "South"],
    [2, "國立臺灣科技大學", "National Taiwan University of Science and Technology", 31600, "North"],
    [3, "國立臺北科技大學", "National Taipei University of Technology", 27887, "North"],
    [4, "國立虎尾科技大學", "National Formosa University", 22684, "South"],
    [5, "國立雲林科技大學", "National Yunlin University of Science and Technology ", 21898, "South"],
    [6, "國立屏東科技大學", "National Pingtung University of Science and Technology", 15972, "South"],
    [7, "國立勤益科技大學", "National Chin-Yi University of Technology ", 15035, "North"],
    [8, "國立臺北護理健康大學", "National Taipei University of Nursing and Health Sciences", 6630, "North"],
    [9, "國立高雄餐旅大學", "National Kaohsiung University of Hospitality and Tourism", 9352, "South"],
    [10, "國立臺北商業大學", "National Taipei University of Business", 6908, "North"],
    [11, "國立臺東專科學校", "National Taitung Junior College", 3168],
    [12, "國立臺中科技大學", "National Taichung University of Science and Technology", 2289, "North"],
    [13, "國立臺灣戲曲學院", "National Taiwan College of Performing Arts", 399, "North"],
    [14, "國立澎湖科技大學", "National Penghu University of Science and Technology", 2715],
    [15, "國立臺南護理專科學校", "National Tainan Junior College of Nursing", 2395, "South"],
])

private_research_centric_university = pd.DataFrame(data=[
    [1, "臺北醫學大學", "Taipei Medical University", 26740, "North"],
    [2, "中國醫藥大學", "China Medical University", 20226, "North"],
    [3, "長庚大學", "Chang Gung University", 16914, "North"],
    [4, "中原大學", "Chung Yuan Christian University", 14880, "North"],
    [5, "高雄醫學大學", "Kaohsiung Medical University", 10052, "South"],
    [6, "逢甲大學", "Feng Chia University", 14313, "North"],
    [7, "東海大學", "Tunghai University", 12358, "North"],
    [8, "元智大學", "Yuan Ze University", 8377, "North"],
    [9, "義守大學", "I-SHOU University", 6854, "South"],
    [10, "東吳大學", "Soochow University", 9579, "North"],
    [11, "輔仁大學", "Fu Jen Catholic University", 8290, "North"],
    [12, "靜宜大學", "Providence University", 8672, "North"],
    [13, "淡江大學", "Tamkang University", 8965, "North"],
    [14, "銘傳大學", "Ming Chuan University", 7368, "North"],
    [15, "中國文化大學", "Chinese Culture University", 6772, "North"],
    [16, "實踐大學", "Shih Chien University", 6632, "North"],
    [17, "亞洲大學", "Asia University", 6370, "North"],
    [18, "大葉大學", "Dayeh University", 6964, "North"],
    [19, "世新大學", "Shih Hsin University", 6016, "North"],
    [20, "中山醫學大學", "Chung Shan Medical University", 5874, "North"],
    [21, "長榮大學", "Chang Jung Christian University", 5397, "South"],
    [22, "南華大學", "Nanhua University", 6012, "South"],
    [23, "慈濟大學", "Tzu Chi University", 5375, "North"],
    [24, "中華大學", "Chung Hua University", 4732, "North"],
    [25, "大同大學", "Tatung University", 3920, "North"],
    [26, "佛光大學", "Fo Guang University", 4842, "North"],
    [27, "馬偕醫學院", "Mackay Medical College", 4306, "North"],
    [28, "華梵大學", "Huafan University", 2887, "North"],
    [29, "玄奘大學", "Hsuan Chuang University", 3917, "North"],
    [30, "中信金融管理學院", "CTBC BUSINESS SCHOOL", 889, "South"],
    [31, "開南大學", "Kainan University", 1871, "North"],
    [32, "真理大學", "Aletheia University", 2154, "North"],
    [33, "台灣首府大學", "Taiwan Shoufu University", 1114, "South"],
    [34, "明道大學", "MingDao University", 1668, "North"],
    [35, "康寧大學", "University of Kang Ning", 1583, "North"],
    [36, "一貫道天皇學院", "I-Kuan Tao College", 517, "South"],
    [37, "法鼓文理學院", "Dharma Drum Institute of Liberal Arts", 381, "North"],
    [38, "稻江科技暨管理學院", "DaouJian Institute", 202, "South"]
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


header2 = ['Number', 'Chinese name', 'English name', 'Budget_received', 'Location']

print(public_vocational_centric_university)

public_vocational_centric_university.columns = header2
print(public_vocational_centric_university)

condition = public_vocational_centric_university['Location'] == "North"
north_public_vocational = public_vocational_centric_university[condition]
print(north_public_vocational)

total_north_public_vocational = north_public_vocational['Budget_received'].sum()
print(total_north_public_vocational)

condition = public_vocational_centric_university['Location'] == "South"
south_public_vocational = public_vocational_centric_university[condition]
print(south_public_vocational)

total_south_public_vocational = south_public_vocational['Budget_received'].sum()
print(total_south_public_vocational)

print(private_research_centric_university)
private_research_centric_university.columns = header2
print(private_research_centric_university)

condition = private_research_centric_university["Location"] == "North"
north_private_research = private_research_centric_university[condition]
print(north_private_research)
total_north_private_research = north_private_research['Budget_received'].sum()
print(total_north_private_research)

condition = private_research_centric_university["Location"] == "South"
south_private_research = private_research_centric_university[condition]
print(south_private_research)

total_south_private_research = south_private_research['Budget_received'].sum()
print(total_south_private_research)

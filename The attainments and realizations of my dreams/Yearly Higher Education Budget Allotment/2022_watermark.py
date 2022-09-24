import pandas as pd
import matplotlib.image as image
import matplotlib.pyplot as plt
# Using the magic encoding
# -*- coding: utf-8 -*-


# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

public_research_centric_university = pd.DataFrame(data=[
    [1, "國立臺灣大學", "National Taiwan University", 232587, "North", ],
    [2, "國立成功大學", "National Cheng Kung University", 141178, "South", ],
    [3, "國立清華大學", "National Tsing Hua University", 120394, "North", "Derived from Beijing, China's Tsing Hua University"],
    [4, "國立陽明交通大學（交大校區）", "National Yang Ming Chiao Tung University (Hsinchu)", 138078, "North", "Derived from Shanghai, China's ChiaoTung University"],
    [5, "國立中興大學", "National Chung Hsing University", 43745, "North", ],
    [6, "國立中央大學", "National Central University", 42228, "North", ],
    [7, "國立陽明交通大學（陽明校區）", "National Yang Ming Chiao Tung University (Taipei)", 0, "North", ],
    [8, "國立政治大學", "National Chengchi University", 31579, "North", "Literally, 'National Politics University'"],
    [9, "國立中山大學", "National Sun Yat-sen University", 32068, "South", ],
    [10, "國立臺灣師範大學", "National Taiwan Normal University", 14233, "North", ],
    [11, "國立中正大學", "National Chung Cheng University", 15361, "South", "Literally, National Chiang Chung-cheng University"],
    [12, "國立臺灣海洋大學", "National Taiwan Ocean University", 14233, "North", ],
    [13, "國立臺北大學", "National Taipei University", 8771, "North", ],
    [14, "國立暨南國際大學", "National Chi Nan University", 8030, "North", ],
    [15, "國立彰化師範大學", "National Changhua University of Education", 7580, "North", ],
    [16, "國立東華大學", "National Dong Hwa University", 6965, "Hualien County", ],
    [17, "國立嘉義大學", "National Chiayi University", 5927, "South", ],
    [18, "國立宜蘭大學", "National Ilan University", 6799, "North", ],
    [19, "國立屏東大學", "National Pingtung University", 6619, "South", ],
    [20, "國立臺東大學", "National Taitung University", 6178, "Taitung County", ],
    [21, "國立臺灣藝術大學", "National Taiwan University of Arts", 5974, "North", ],
    [22, "國立臺北教育大學", "National Taipei University of Education", 5234, "North", ],
    [23, "國立高雄大學", "National University of Kaohsiung", 5502, "South", ],
    [24, "國立臺北藝術大學", "The Taipei National University of the Arts", 5478, "North", ],
    [25, "國立臺中教育大學", "National Taichung University of Education", 5549, "North", ],
    [26, "國立臺南大學", "National University of Tainan", 5203, "South", ],
    [27, "臺北市立大學", "University of Taipei", 5247, "North", ],
    [28, "國立體育大學", "National Taiwan Sport University", 4732, "North", ],
    [29, "國立聯合大學", "National United University", 4676, "North", ],
    [30, "國立高雄師範大學", "National Kaohsiung Normal University", 4347, "South", ],
    [31, "國立臺灣體育運動大學", "National Taiwan University of Sport", 3229, "North", ],
    [32, "國立金門大學", "National Quemoy University", 3319, ],
    # [33, "國立臺灣體育運動大學", "National Taiwan University of Sport", 3226, "North", ],
    [33, "國立臺南藝術大學", "Tainan National University of the Arts", 1997, "South", ],
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
plt.bar(['Northern Taiwan', 'Southern Taiwan'], [total_north_public_research, total_south_public_research])

plt.xlabel('Location (divided by Zhuoshui River)\n\n'
           'Dataset: https://sprout.moe.edu.tw/SproutWeb/Project/DocDownload',
           fontproperties="Arial", fontsize=9)

plt.ylabel('Unit: 10 thousands of New Taiwan Dollar')
plt.title('Government budget support for public research universities (國立大學)\n'
          'in North vs South in 2022', fontproperties="MS Gothic")

# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=800, yo=800, alpha=0.9)

# Insert text watermark
plt.text(x=0.6, y=0.7, s="CC-BY 4.0", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation='30', transform=ax.transAxes)

plt.show()
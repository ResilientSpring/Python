import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
# Using the magic encoding
# -*- coding: utf-8 -*-


# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

university = pd.DataFrame(data=[
    [1, "國立臺灣大學", "National Taiwan University", 300000, "North", ],
    [2, "國立成功大學", "National Cheng Kung University", 170000, "South", ],
    [3, "國立清華大學", "National Tsing Hua University", 100000, "North", "Derived from Beijing, China's Tsing Hua University"]
])

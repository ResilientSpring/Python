import pandas as pd

importation = pd.DataFrame(columns=["基隆關", "臺北關", "臺中關", "高雄關", "合計"],
                           index=["進口報單申報完稅價格(包含小三通)", "進口快遞貨物完稅價格", "進口快遞簡易完稅價格"],
                           data=[[1887315195, 3744420037, 1317064881, 1685399059, 8634199171],
                                 [2249153, 952141962, 0, 1411, 954392527],
                                 [5639340, 38349842, 0, 268237, 44257418]])
print(importation)

total_importation = importation.sum(axis=0)
print(total_importation)

print(1685399059 + 1411 + 268237)

importation2 = importation.append(total_importation, ignore_index=True)
print(importation2)

print(importation2.iloc[:, 0])

importation2.index = ["進口報單申報完稅價格(包含小三通)", "進口快遞貨物完稅價格", "進口快遞簡易完稅價格", "Sum of the customs"]
print(importation2)

print(importation2.iloc[:, 0])

importation2.to_csv("2020_import_value_from_each_customs.csv")

import pandas as pd

importation = pd.DataFrame(columns=["基隆關", "臺北關", "臺中關", "高雄關", "合計"],
                           index=["進口報單申報完稅價格(包含小三通)", "進口快遞貨物完稅價格", "進口快遞簡易完稅價格"],
                           data=[[1887315195, 3744420037, 1317064881, 1685399059, 8634199171],
                                 [2249153, 952141962, 0, 1411, 954392527],
                                 [5639340, 38349842, 0, 268237, 44257418]])
print(importation)

exportation = pd.DataFrame(data=[[1544095246, 5561724423, 2550413664, 3030786960, 12687020293],
                                 [5497, 1093775143, 0, 0, 1093780640],
                                 [571, 19273738, 0, 0, 19274309]],
                           columns=["基隆關", "臺北關", "臺中關", "高雄關", "合計"],
                           index=["出口貨物離岸價格(包含小三通)", "出口快遞貨物離岸價格", "出口快遞簡易離岸價格"])

print(exportation)

total_exportation = exportation.sum(axis=0)
print(total_exportation)

exportation2 = exportation.append(total_exportation, ignore_index=True)
print(exportation2)

print(exportation2.iloc[:, 0])

exportation2.index = ["出口貨物離岸價格(包含小三通)", "出口快遞貨物離岸價格", "出口快遞簡易離岸價格", "Sum of the customs"]
print(exportation2)

print(exportation2.iloc[:, 0])

exportation2.to_csv("2020_export_value_from_each_customs.csv")

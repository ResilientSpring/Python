import matplotlib.pyplot as plt
import matplotlib.image as image

year = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
income_Kaohsiung = [1145895, 1166824, 1186204, 1219246, 1224268, 1224100, 1231562]
income_Tainan = [1007093, 1063495, 1079199, 1086077, 1079174, 1086475, 1120580]
income_Taichung = [1169183, 1140325, 1245350, 1279865, 1298497, 1289700, 1304508]
income_Taoyuan = [1307158, 1317790, 1337361, 1378732, 1392199, 1424027, 1448909]
income_Taipei = [1581899, 1568945, 1648122, 1649348, 1723021, 1716591, 1732126]
income_New_Taipei = [1171978, 1223867, 1265798, 1292753, 1319841, 1352548, 1381603]
income_Hsinchu_county = [1283995, 1365150, 1616327, 1519478, 1539555, 1619782, 1689337]
income_Hsinchu_city = [1427572, 1537317, 1572296, 1426379, 1602826, 1618903, 1602415]
# income_Miaoli_county = [1008241, 1166196, 1029485, 1045881, 1073028, 1161999, 1214424]

fig, ax = plt.subplots(figsize=(9, 9))

plt.plot(year, income_Taipei, label="Taipei")
plt.plot(year, income_New_Taipei, label="New Taipei")
plt.plot(year, income_Taoyuan, label="Taoyuan")
plt.plot(year, income_Hsinchu_county, label="Hsinchu county")
plt.plot(year, income_Hsinchu_city, label="Hsinchu city")
# plt.plot(year, income_Miaoli_county, label="Miaoli")
plt.plot(year, income_Taichung, label="Taichung")
plt.plot(year, income_Tainan, label="Tainan")
plt.plot(year, income_Kaohsiung, label="Kaohsiung", marker='*', ms=12)

plt.title("Annual household income by region in Taiwan")
plt.legend()
plt.grid(linewidth=0.7)
plt.ylabel("Income (1 million New Taiwan Dollar)")
plt.xlabel("Reference: https://statfy.mol.gov.tw/map02.aspx?cid=64&xFunc=138&xKey=1")

img = image.imread('CC-BY.png')

plt.figimage(X=img, xo=800, yo=800, alpha=0.9)

# Insert text watermark [1]
plt.text(x=0.6, y=0.7, s="CC-BY 4.0", fontsize=40, color='grey', alpha=0.9,
         ha='center', va='center', rotation='30', transform=ax.transAxes)

plt.show()

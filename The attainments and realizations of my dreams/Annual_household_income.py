import matplotlib.pyplot as plt

year = [2015, 2016, 2017, 2018, 2019, 2020]
income_Kaohsiung = [1145895, 1166824, 1186204, 1219246, 1224268]
income_Tainan = [1007093, 1063495, 1079199, 1086077, 1079174, 1086475]
income_Taichung = [1169183, 1140325, 1245350, 1279865, 1298497, 1289700]
income_Taoyuan = [1307158, 1317790, 1337361, 1378732, 1392199, 1424027]
income_Taipei = [1581899, 1568945, 1648122, 1649348, 1723021, 1716591]
income_New_Taipei = [1171978, 1223867, 1265798, 1292753, 1319841, 1352548]

plt.plot(year, income_Taipei)
plt.plot(year, income_New_Taipei)
plt.plot(year, income_Taoyuan)
plt.plot(year, income_Taichung)
plt.plot(year, income_Tainan)
plt.plot(year, income_Kaohsiung)

plt.show()

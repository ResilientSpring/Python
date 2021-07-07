import pandas as pd

df = pd.read_csv('year2018.csv', encoding='big5', header=1, skipinitialspace=True, skiprows=0) #[1][2][3]
print(df)

# References:
# 1. https://sprout.moe.edu.tw/SproutWebAPI/api/DocDownload/DownladFile/VSVt4Rr2ptU%3d
# 2. https://web.archive.org/web/20200925142828/https://ithelp.ithome.com.tw/articles/10232726
# 3. https://web.archive.org/web/20210302012218/https://thispointer.com/pandas-skip-rows-while-reading-csv-file-to-a-dataframe-using-read_csv-in-python/

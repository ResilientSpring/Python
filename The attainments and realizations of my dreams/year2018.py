import pandas as pd

df = pd.read_csv('year2018.csv', encoding='big5', header=1, skipinitialspace=True,
                 skiprows=0, skip_blank_lines=True, nrows=71, index_col=['學校代碼']) #[1][2][3][4]
print(df)

df.to_csv('year2018_public_research.csv')

# References:
# 1. https://sprout.moe.edu.tw/SproutWebAPI/api/DocDownload/DownladFile/VSVt4Rr2ptU%3d
# 2. https://web.archive.org/web/20200925142828/https://ithelp.ithome.com.tw/articles/10232726
# 3. https://web.archive.org/web/20210302012218/https://thispointer.com/pandas-skip-rows-while-reading-csv-file-to-a-dataframe-using-read_csv-in-python/
# 4. https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

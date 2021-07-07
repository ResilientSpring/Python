import pandas as pd

url = 'https://sprout.moe.edu.tw/SproutWebAPI/api/DocDownload/DownladFile/VSVt4Rr2ptU%3d'
df = pd.read_csv(url)
print(df)

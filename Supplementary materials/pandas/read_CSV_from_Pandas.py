import pandas as pd

url = "https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv";
df = pd.read_csv(url, index_col=0);
print(df.head(5));

# Reference:
# https://stackoverflow.com/questions/55240330/how-to-read-csv-file-from-github-using-pandas
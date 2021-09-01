import pandas as pd

# Column(s) to use as the row labels of the DataFrame, either given as string name or column index.
# If a sequence of int / str is given, a MultiIndex is used.[1]
df = pd.read_csv("2020_November_daily_mobile_user_distribution_by_county.csv"
                 , header=0, skiprows=[1], encoding="big5", index_col=["COUNTY"])

print(df)

new = df.drop(labels=["COUNTY_ID"], axis=1)
print(new)

new.to_csv('2020_Nov_daily_mobile_user_distribution_by_county_.csv')

# References:
# 1. https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.read_csv.html

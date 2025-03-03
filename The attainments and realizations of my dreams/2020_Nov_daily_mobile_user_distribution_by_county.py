import pandas as pd

# Skip one or more rows by giving the row indices (the first row that's not skipped is the header):[1]
df = pd.read_csv("2020_November_daily_mobile_user_distribution_by_county.csv"
                 , header=0, skiprows=[1], encoding="big5")

print(df)

# References:
# 1. https://stackoverflow.com/a/27325729/14900011

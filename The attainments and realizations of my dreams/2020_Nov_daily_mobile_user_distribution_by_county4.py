import pandas as pd

# Skip one or more rows by giving the row indices (the first row that's not skipped is the header):[1]
df = pd.read_csv("2020_November_daily_mobile_user_distribution_by_county.csv"
                 , header=0, skiprows=[1], encoding="big5")

print(df)

new = df.drop(labels=["COUNTY_ID"], axis=1)
print(new)

branding = new.reset_index().set_index('COUNTY')
print(branding)

# References:
# 1. https://stackoverflow.com/a/27325729/14900011

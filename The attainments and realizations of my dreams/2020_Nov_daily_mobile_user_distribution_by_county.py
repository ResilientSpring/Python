import pandas as pd

df = pd.read_csv("2020_November_daily_mobile_user_distribution_by_county.csv"
                 , header=0, skiprows=1)

print(df)

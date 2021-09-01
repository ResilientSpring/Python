import pandas as pd

dataframe = pd.read_csv('2020_Nov_daily_mobile_user_distribution_by_county_.csv', header=0,
                        index_col=["COUNTY"])
print(dataframe)

total = dataframe["NIGHT_WORK"].sum()
print(total)

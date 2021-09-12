import pandas as pd

distribution = pd.read_csv('2020_translated_Nov_daily_mobile_user_distribution_by_county_.csv',
                           index_col=0)

print(distribution.head())

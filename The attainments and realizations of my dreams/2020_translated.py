import pandas as pd
import matplotlib.pyplot as plt

distribution = pd.read_csv('2020_translated_Nov_daily_mobile_user_distribution_by_county_.csv',
                           index_col=0)

print(distribution.head())
print(30*'=')
print(distribution.info())
print(30*'=')
print(distribution["INFO_TIME"].value_counts())
print(30*'=')
print(distribution.describe())
print(30*'=')
print(distribution.hist(bins=50, figsize=(20, 15)))
plt.savefig('2020_translated_histogram')
plt.show()

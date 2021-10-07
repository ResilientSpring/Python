import pandas as pd
import matplotlib.pyplot as plt

distribution = pd.read_csv('2020_translated_Nov_daily_mobile_user_distribution_by_county_.csv',
                           index_col=0)

transposed_distribution = distribution.transpose()
print(transposed_distribution)
transposed_distribution.to_csv("2020_transposed_translated_mobile_user_distribution_by_county.csv")

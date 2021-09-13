import pandas as pd
import matplotlib.pyplot as plt

distribution = pd.read_csv('2020_transposed_translated_mobile_user_distribution_by_county.csv',
                            index_col=0)
print(distribution)

print(distribution.info())

import pandas as pd
import matplotlib.pyplot as plt

distribution = pd.read_csv('2020_transposed_translated_mobile_user_distribution_by_county.csv',
                           index_col=0, header=0, skiprows=0)
print(distribution)

distribution = pd.read_csv('2020_transposed_translated_mobile_user_distribution_by_county.csv',
                           index_col=0, skiprows=0, header=0)
print(distribution)

distribution = pd.read_csv('2020_transposed_translated_mobile_user_distribution_by_county.csv',
                           index_col=0, skiprows=[0], header=0)
print(distribution)

distribution = pd.read_csv('2020_transposed_translated_mobile_user_distribution_by_county.csv',
                           index_col=0, header=0, skiprows=[0])
print(distribution)

distribution = pd.read_csv('2020_transposed_translated_mobile_user_distribution_by_county.csv',
                           index_col=0, header=0, skiprows=1)
print(distribution)

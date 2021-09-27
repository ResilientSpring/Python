import pandas as pd
import matplotlib.pyplot as plt

exportation = pd.read_csv("2020_export_value_from_each_customs.csv", header=0, index_col=0)

print(exportation)
print(exportation.info())

def TW_to_USD(x):
    """
    TWD	Taiwan New Dollar	28.0881028819	0.0356022621

    https://web.archive.org/web/20210927101148/https://www.xe.com/currencytables/?from=USD&date=2020-12-31
    """
    return x / 28.0881028819


exportation_USD = exportation.applymap(TW_to_USD)

print(exportation_USD)

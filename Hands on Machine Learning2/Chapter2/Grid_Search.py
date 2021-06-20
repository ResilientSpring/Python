import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

housing = pd.read_csv(filepath_or_buffer=url, header=0)

print(housing)
print(housing.info())
print(housing.describe())

housing.hist(bins=50, figsize=(20, 15))
plt.savefig('histogram for numeric attribute.jpg')
plt.show()

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(test_set.head())

housing["median_income"].hist()
plt.savefig('histogram for a column.jpg')
plt.show()

housing["income_cat"] = pd.cut(housing["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])

print(housing["income_cat"].value_counts())

housing["income_cat"].hist()
plt.savefig('histogram for column income_cat.jpg')
plt.show()

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

    print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))
    print(housing["income_cat"].value_counts() / len(housing))




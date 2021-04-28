from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd

# Loading some example data
iris = datasets.load_iris()

print(iris)

# Put data into data frame to improve readability
iris_df = pd.DataFrame(data=datasets.load_iris().data)
print(iris_df)

# Rename the column
new_iris_df = iris_df.rename(columns={0: "sepal length ", 1:"sepal width", 2: "petal length",
                                      3: "petal width"})  # [1]

print(new_iris_df)

# Concatenate the target column to new_iris_df
new_iris_df["target"] = datasets.load_iris().target
print(new_iris_df)



# References:
# 1. https://www.dataindependent.com/pandas/pandas-change-column-names/
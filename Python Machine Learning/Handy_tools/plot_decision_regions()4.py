from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd

# Loading some example data
iris = datasets.load_iris()

print(iris)

iris_df = pd.DataFrame(data=datasets.load_iris().data)
print(iris_df)

iris_df.reindex(labels=["sepal length in cm", "sepal width in cm", "petal length in cm",
                        "petal width in cm"], axis=1)

print(iris_df)

new_iris_df = iris_df.rename(columns={0: "sepal length ", 1:"sepal width", 2: "petal length",
                        3: "petal width"})

print(new_iris_df)
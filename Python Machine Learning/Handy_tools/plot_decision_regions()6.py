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
new_iris_df = iris_df.rename(columns={0: "sepal length", 1: "sepal width", 2: "petal length",
                                      3: "petal width"})

print(new_iris_df)

# Concatenate the target column to new_iris_df in order to see the full extent of the data.
new_iris_df["target"] = datasets.load_iris().target
print(new_iris_df)

# Pick "sepal length" and "petal length" as the features.
X = new_iris_df.filter(items=["sepal length", "petal length"])
print(X)

# Class set
y = new_iris_df.filter(items=["target"])

# Initialized the classifier
svm = SVC(C=0.5, kernel="linear")

# Train the classifier
svm.fit(X=X, y=y)

# Plotting decision regions
plot_decision_regions(X=X, y=y, clf=svm, legend=2)

# Adding axes annotations
plt.xlabel("sepal length [cm]")
plt.ylabel("petal length [cm]")
plt.title("SVM on Iris")
plt.show()

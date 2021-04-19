from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()

# feature set
iris_data = iris.data
print(iris_data)

# class set
iris_label = iris.target
print(iris_label)

# split dataset into training set and test set.
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label,
                                                                  test_size=0.2);
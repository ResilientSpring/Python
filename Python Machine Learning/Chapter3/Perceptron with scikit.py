from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

iris = datasets.load_iris();
print(iris);
print(type(iris));

# Assign the petal length and petal width of the 150 flower examples to the feature matrix X.
X = iris.data[:, [2, 3]];

# Assign the class labels of the flower species to the vector array y.
y = iris.target;

print("Class labels: ", np.unique(y));

# Split the dataset into seperate training and test dataset

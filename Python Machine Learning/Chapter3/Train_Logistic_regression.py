from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
import Logistic_Regression
import Decision_boundary_visualization as visualization
import matplotlib.pyplot as plt

iris = datasets.load_iris();
print(iris);
print(type(iris));

# Assign the petal length and petal width of the 150 flower examples to the feature matrix X.
X = iris.data[:, [2, 3]];

# Assign the class labels of the flower species to the vector array y.
y = iris.target;

print("Class labels: ", np.unique(y));

# Split the dataset into separate training and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1,
                                                    stratify=y);

print("Labels counts in y:", np.bincount(y));
print("Labels counts in y_train:", np.bincount(y_train));
print("Labels counts in y_test:", np.bincount(y_test));

# feature scaling
sc = StandardScaler();
sc.fit(X=X_train);
X_train_std = sc.transform(X=X_train);
X_test_std = sc.transform(X=X_test);

X_train_01_subset = X_train[(y_train == 0) | (y_train == 1)];
y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)];

lrgd = Logistic_Regression.LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1);
lrgd.fit(X=X_train_01_subset, y=y_train_01_subset);

visualization.plot_decision_regions(X=X_train_01_subset, y=y_train_01_subset,
                                    classifier=lrgd);

plt.xlabel("petal length [standardized]");
plt.ylabel("petal width [standardized]");
plt.legend(loc="upper left");
plt.tight_layout();

plt.savefig("logistic_regression.jpg");

plt.show();
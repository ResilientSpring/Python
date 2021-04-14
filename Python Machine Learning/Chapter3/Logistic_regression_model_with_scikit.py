from sklearn.linear_model import LogisticRegression
import plot

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

lr = LogisticRegression(C=100.0, random_state=1, solver="lbfgs", multi_class="ovr");

lr.fit(X=X_train_std, y=y_train);
visualization.plot_decision_regions(X=plot.X_combined_std, y=plot.y_combined, classifier=lr,
                                    test_idx=range(105, 150));
plt.xlabel("petal length [standardized]");
plt.ylabel("petal width [standardized]");
plt.legend(loc="upper left");
plt.tight_layout();

plt.show();
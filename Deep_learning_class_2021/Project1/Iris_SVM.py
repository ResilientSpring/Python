from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import numpy as np
from sklearn.model_selection import cross_val_score

iris = load_iris()
iris_data=iris.data
print(iris_data)
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris.target, test_size=0.33);

print(X_train.shape)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

svm_reg = svm.SVR()
regressor = svm_reg.fit(X=X_train, y=y_train)

y_prediction = svm_reg.predict(X=X_test)

print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_prediction));
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_prediction));
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_prediction)));

score = cross_val_score(estimator=svm.SVC(random_state=1))
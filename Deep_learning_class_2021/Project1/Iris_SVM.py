from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm

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
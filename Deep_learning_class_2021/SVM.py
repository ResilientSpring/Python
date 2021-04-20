from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

iris = load_iris()

iris_data = iris.data
print(iris_data)

iris_label = iris.target
print(iris_label)

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label,
                                                                  test_size=0.2, random_state=0)

# initialize the algorithm object
clf = svm.SVC()

# Train it
clf.fit(X=train_data, y=train_label)

y_prediction = clf.predict(X=test_data)

print("Prediction: ", y_prediction)
print("Test labels:", test_label)

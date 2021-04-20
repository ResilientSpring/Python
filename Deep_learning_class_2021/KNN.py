from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

iris_label = iris.target
iris_data = iris.data

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label,
                                                                  test_size=0.2, random_state=0)
# Initialize the algorithm object
knn = KNeighborsClassifier(n_neighbors=3)

# Let's train!
knn.fit(X=train_data, y=train_label)

y_prediction = knn.predict(X=test_data)

print("Prediction: ", y_prediction)

print("GroundTruth:", test_label)


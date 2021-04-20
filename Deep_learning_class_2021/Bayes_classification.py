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

# Train the Bayesian algorithm

## Initialization
clf = GaussianNB();

## Find the parameters
clf.fit(X=train_data, y=train_label);

## Make the predictions
y_prediction = clf.predict(X=test_data)

## Show the prediction
print(y_prediction);

# Print the prediction
print("Predict: ", y_prediction)

## Show the ground truth
print("Answer:  ", test_label)
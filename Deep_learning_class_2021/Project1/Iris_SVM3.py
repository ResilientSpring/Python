from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, classification_report, accuracy_score

iris = load_iris()
iris_data = iris.data
iris_label = iris.target
print(iris_data)

pipeline = make_pipeline(StandardScaler(), svm.SVC(random_state=1))
pipeline.fit(X=iris_data, y=iris.target)

y_prediction_Scaled = pipeline.predict(X=iris_data)

score = cross_val_score(estimator=pipeline, X=iris_data, y=iris.target, cv=10, scoring="accuracy")
print("Array of accuracy of the estimator for each run of the cross validation: ", score)
print("Mean accuracy: ", score.mean())

X_train, y_train, X_test, y_test = train_test_split(iris_data, iris.target, test_size=0.33,
                                                    random_state=1)



target_names = ['setosa', 'veriscolor', 'virginica']

print("Accuracy score: ", accuracy_score(iris.target.prediction))
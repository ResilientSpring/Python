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
print(iris_data)

pipeline = make_pipeline(StandardScaler(), svm.SVC(random_state=1))
pipeline.fit(X=iris_data, y=iris.target)

y_prediction_Scaled = pipeline.predict(X=iris_data)


print("Mean Absolute Error (after scaling input data):", metrics.mean_absolute_error(iris.target, y_prediction_Scaled));
print("Mean Squared Error (after scaling input data):", metrics.mean_squared_error(iris.target, y_prediction_Scaled));
print("Root Mean Squared Error (after scaling input data):",
      np.sqrt(metrics.mean_squared_error(iris.target, y_prediction_Scaled)))

score = cross_val_score(estimator=pipeline, X=iris_data, y=iris.target, cv=10, scoring="accuracy")
print("Array of accuracy of the estimator for each run of the cross validation: ", score)
print("Mean accuracy: ", score.mean())

print("Confusion matrix: ", confusion_matrix(y_true=iris.target, y_pred=y_prediction_Scaled))
print("Precision score: ", precision_score(y_true=iris.target, y_pred=y_prediction_Scaled))
print("Recall: ", recall_score(y_true=iris.target, y_pred=y_prediction_Scaled))
print("F1: ", f1_score(y_true=iris.target, y_pred=y_prediction_Scaled))

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import numpy as np

cancer_data = load_breast_cancer()

X = cancer_data.data
y = cancer_data.target

print('Input data size: ', X.shape)
print('Output data size: ', y.shape)

# Check to see if it's a binary or multi-class classification.
print('Label names: ', cancer_data.target_names)

# Determine if the data distribution among the dataset is balanced.
n_positive = (y == 1).sum()
n_negative = (y == 0).sum()
print(f'{n_positive} positive samples and {n_negative} negative samples.')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.33)

# linear is chosen for binary classification.
classifier = SVC(C=5.0, kernel='linear', random_state=42)
classifier.fit(X=X_train, y=y_train)

y_prediction = classifier.predict(X=X_test)

accuracy = classifier.score(X=X_test, y=y_test)

print("The accuracy is: {:.2f}".format(accuracy * 100))

print("Classification report: ", '\n', classification_report(y_true=y_test,
                                                             y_pred=y_prediction,
                                                             target_names=['malignant', 'benign']))

scores = cross_val_score(estimator=classifier, cv=10, X=X_train, y=y_train, scoring='accuracy')
print("10-fold cross validation Scores: ", scores)
print("Mean Scores: ", scores.mean())

y_prediction2 = classifier.predict(X=X_train)

print("Classification report after 10-fold cross validation: ", '\n',
      classification_report(y_true=y_train,
                            y_pred=y_prediction2,
                            target_names=['malignant', 'benign']))

accuracy2 = classifier.score(X=X_train, y=y_train)
print("The accuracy is: {:.2f}".format(accuracy2 * 100))

from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report

face_data = fetch_lfw_people(min_faces_per_person=80)

X = face_data.data
y = face_data.target
print('Input data size: ', X.shape)
print('Output data size: ', y.shape)
print('Label names: ', face_data.target_names)

# Analyze the label distribution (Determine if the data distribution among the dataset is balanced.)
for i in range(5):
    print(f'Class {i} has {(y == i).sum()} samples.')


fig, ax = plt.subplots(3, 4)
for i, axi in enumerate(ax.flat):
    axi.imshow(face_data.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=face_data.target_names[face_data.target[i]])


plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

SVM_classifier = SVC(class_weight='balanced', random_state=42)

parameters = {'C': [0.1, 1, 10], 'gamma': [1e-07, 1e-08, 1e-06], 'kernel': ['rbf', 'linear']}

grid_search = GridSearchCV(estimator=SVM_classifier, param_grid=parameters, cv=5)
grid_search.fit(X=X_train, y=y_train)

print('The best model: \n', grid_search.best_params_)

print('The best averaged performance: ', grid_search.best_score_)

best_classifier = grid_search.best_estimator_

y_prediction = best_classifier.predict(X=X_test)

print(f'The accuracy is: {best_classifier.score(X_test, y_test)*100:.1f}%')

print(classification_report(y_true=y_test, y_pred=y_prediction,
                            target_names=face_data.target_names))

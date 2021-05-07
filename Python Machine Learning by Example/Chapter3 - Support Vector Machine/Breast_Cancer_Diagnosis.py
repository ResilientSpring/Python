from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

cancer_data = load_breast_cancer()

X = cancer_data.data
Y = cancer_data.target

print('Input data size: ', X.shape)
print('Output data size: ', Y.shape)
print('Label names: ', cancer_data.target_names)

n_pos = (Y == 1).sum()
n_neg = (Y == 0).sum()
print(f'{n_pos} positive samples and {n_neg} negative samples.')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

classifier = SVC(C=1.0, kernel='linear', random_state=42)

classifier.fit(X=X_train, y=Y_train)

y_prediction = classifier.predict(X=X_test)

accuracy = classifier.score(X=X_test, y=Y_test)

print(f'The accuracy is: {accuracy*100:.1f}%')


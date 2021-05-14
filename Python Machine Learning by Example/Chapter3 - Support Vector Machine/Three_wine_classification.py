from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

wine_data = load_wine()
X = wine_data.data
y = wine_data.target
print("Input size: ", X.shape)
print('Output size: ', y.shape)

print('Label names: ', wine_data.target_names)

n_of_class0 = (y == 0).sum()
n_of_class1 = (y == 1).sum()
n_of_class2 = (y == 2).sum()

print(f'{n_of_class0} class0 samples,\n{n_of_class1} class1 samples,\n{n_of_class2} class2 samples.')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = SVC(kernel='linear', C=1.0, random_state=42)

clf.fit(X=X_train, y=y_train)

accuracy = clf.score(X=X_test, y=y_test)

print(accuracy)

y_prediction = clf.predict(X=X_test)

print(classification_report(y_true=y_test, y_pred=y_prediction))

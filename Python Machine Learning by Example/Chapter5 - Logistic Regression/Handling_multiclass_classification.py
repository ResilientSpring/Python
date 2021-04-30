from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import SGDClassifier

digits = datasets.load_digits()

n_samples = len(digits.images)

# As the image data is stored in 8 x 8 matrices, we need to flatten them.
X = digits.images.reshape((n_samples, -1))

Y = digits.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

parameters = {"penalty": ["l2", None], "alpha": [1e-07, 1e-06, 1e-05, 1e-04],
              "eta0": [0.01, 0.1, 1, 10]}

sgd_lr = SGDClassifier(loss="log", learning_rate="constant", eta0=0.01, fit_intercept=True,
                       max_iter=10)

grid_search = GridSearchCV(sgd_lr, parameters, n_jobs=1, cv=3)
grid_search.fit(X_train, Y_train)
print(grid_search.best_params_)

sgd_lr_best = grid_search.best_estimator_
accuracy = sgd_lr_best.score(X_test, Y_test)
print(f"The accuracy on testing set is: {accuracy * 100:.1f}")

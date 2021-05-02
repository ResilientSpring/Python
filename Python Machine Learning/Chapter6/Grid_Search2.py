from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import Data_pre_processing as dataset

pipe_svc = make_pipeline(StandardScaler(), SVC(random_state=1))

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

param_grid = [{'svc__C': param_range, 'svc__kernel': ['linear']},
              {'svc__C': param_range, 'svc__gamma': param_range, 'svc__kernel': ['rbf']}]

gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring="accuracy",
                  cv=10, refit=True)

gs = gs.fit(X=dataset.X_train, y=dataset.y_train)

print("GS.best_score", gs.best_score_)

print("GS_best_parameter", gs.best_params_)

# Finally, we use the independent test dataset to estimate the performance of the
# best-selected model, which is available via the best_estimator_ attribute of
# the GridSearchCV object.
clf = gs.best_estimator_
clf.fit(dataset.X_train, dataset.y_train)
print("Test accuracy: ", clf.score(dataset.X_test, dataset.y_test))

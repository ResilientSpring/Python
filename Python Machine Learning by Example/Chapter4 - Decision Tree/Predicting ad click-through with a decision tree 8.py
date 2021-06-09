import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

the_number_of_rows_to_read = 300000
dataset = pd.read_csv(filepath_or_buffer='train.csv', nrows=the_number_of_rows_to_read)

print(dataset.info())
print(dataset.head(50))
print(dataset.tail(50))
print(dataset.describe())

y = dataset['click']

print(y)
print(y.info())
print(y.describe())
print((y == 1).sum())

X = dataset.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)

print(X)
print(X.shape)

X = X.values
y = y.values

the_number_of_training_samples = int(the_number_of_rows_to_read * 0.9)

X_train = X[:the_number_of_training_samples]
print('X_train:', "\n", X_train)

y_train = y[:the_number_of_training_samples]
print('y_train:', '\n', y_train)

X_test = X[the_number_of_training_samples:]
y_test = y[the_number_of_training_samples:]

enc = OneHotEncoder(handle_unknown='ignore')

X_train_enc = enc.fit_transform(X=X_train)

print(type(X_train_enc))

print(X_train_enc[0])

X_test = enc.transform(X=X_test)

# Options for the maximal depth:
parameters = {'max_depth': [3, 10, None]}

decision_tree = DecisionTreeClassifier(criterion='gini', min_samples_split=30)

grid_search = GridSearchCV(estimator=decision_tree, param_grid=parameters, cv=3,
                           scoring='roc_auc', n_jobs=-1)

grid_search.fit(X=X_train, y=y_train)

print(grid_search.best_params_)

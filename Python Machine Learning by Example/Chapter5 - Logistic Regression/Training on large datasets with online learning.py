import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import SGDClassifier
import timeit

df = pd.read_csv('trainee.csv')
print(df)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)
print(X)
print(X.shape)

X = X.values
print(X)

Y = df['click']
print(Y)

Y = Y.values
print(Y)

number_of_train = 10000 * 10

X_train = X[:number_of_train]
Y_train = Y[:number_of_train]
X_test = X[number_of_train:]
Y_test = Y[number_of_train:]

enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(X=X_train)

sgd_online_learning = SGDClassifier(loss='log', penalty=None, fit_intercept=True, max_iter=1,
                                    learning_rate='constant', eta0=0.01)

start_time = timeit.default_timer()

for i in range(9):
    x_train = X_train[i * 100000 : (i + 1) * 100000]
    y_train = Y_train[i * 100000 : (i + 1) * 100000]

    x_train_enc = enc.transform(X=x_train)
    sgd_online_learning.partial_fit(X=x_train_enc.toarray(), y=y_train, classes=[0, 1])

    print(f'---{(timeit.default_timer()) - start_time}.3fs seconds ---')


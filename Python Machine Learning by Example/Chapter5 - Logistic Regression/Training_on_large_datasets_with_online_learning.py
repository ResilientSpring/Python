import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.optimizers import SGD
from sklearn.linear_model import SGDClassifier
import timeit

n_rows = 100000 * 11

df = pd.read_csv(filepath_or_buffer='train.csv', nrows=n_rows)

print(df)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)

print(X)

X_train = X.to_numpy()

print(X_train)

y = df['click']

print(y)

y_train = df['click'].to_numpy()

print(y_train)

enc = OneHotEncoder(handle_unknown='ignore')

enc.fit(X=X_train)

Stochastic_Gradient_Descent_online_learning = SGDClassifier(loss='log', penalty=None,
                                                            fit_intercept=True, max_iter=1,
                                                            learning_rate='constant', eta0=0.01)

X_train_enc = enc.transform(X=X_train)

Stochastic_Gradient_Descent_online_learning.partial_fit(X=X_train_enc.toarray(), y=y_train,
                                                        classes=[0, 1])

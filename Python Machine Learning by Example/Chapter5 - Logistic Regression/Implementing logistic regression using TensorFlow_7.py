import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from tensorflow.keras.optimizers import Adam

# Read in the first 6000 rows.
df = pd.read_csv('train.csv', nrows=6000)
print(df)

X = df.drop(['click', 'id', 'hour', 'device_id', 'device_ip'], axis=1)
print(X)

y = df['click']
print(y)

X_train = X[: int(6000 * 0.9)] # Use 90% of the read-in rows for training.
y_train = y[: int(6000 * 0.9)]

X_test = X[int(6000 * 0.9) :]
y_test = y[int(6000 * 0.9) :]

# Convert Pandas.Dataframe to NumPy array because Tensor is only compatible with NumPy array.
X_train = X_train.to_numpy()
y_train = y_train.to_numpy().astype('float32')

print(X_train)

X_test = X_test.to_numpy()  # We cannot convert the array containing words to float32.
y_test = y_test.to_numpy().astype('float32')

enc = OneHotEncoder(handle_unknown='ignore')

X_train_enc = enc.fit_transform(X=X_train)
print(X_train_enc)  # It hasn't been enclosed in an array.

X_train_enc = enc.fit_transform(X=X_train).toarray().astype('float32') # Enclosing it within an array and convert the encoded words to float32.
print(X_train_enc)

# Scaling the data
X_test_enc = enc.transform(X=X_test)

print(len(X_train_enc))

train_data = tf.data.Dataset.from_tensor_slices((X_train_enc, y_train))
train_data = train_data.repeat().shuffle(len(X_train_enc)).batch(batch_size=1000).prefetch(buffer_size=1)

# Define the weights and bias of the logistic regression model:
number_of_features = int(X_train_enc.shape[1])
weight = tf.Variable(tf.zeros([number_of_features, 1]))
bias = tf.Variable(tf.zeros([1]))

optimizer = Adam(learning_rate=0.0008)

# Define the optimization process where we compute the current prediction and cost and
# update the model following the computed gradients.
def run_optimization(x, y):
    with tf.GradientTape() as g:
        logits = tf.add(tf.matmul(x, weight), bias)[:, 0]
        cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=logits))
    gradient = g.gradient(cost, [weight, bias])
    optimizer.apply_gradients(zip(gradient, [weight, bias]))


training_steps = 6000
for step, (batch_x, batch_y) in enumerate(train_data.take(training_steps), 1):
    run_optimization(batch_x, batch_y)
    if step % 500 == 0:
        logits = tf.add(tf.matmul(batch_x, weight), bias)[:, 0]
        loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=batch_y, logits=logits))
        print("step: %i, loss: %f" % (step, loss))


logits = tf.add(tf.matmul(X_test_enc.shape[0], weight), bias)[:, 0]
prediction = tf.nn.sigmoid(logits)
auc_metric = tf.keras.metrics.AUC()
auc_metric.update_state(y_test, prediction)

print(f'AUC on testing set: {auc_metric.result().numpy():.3f}')

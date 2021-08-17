import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras import layers, models, losses, optimizers
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

vocabulary_size = 5000

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocabulary_size)

# Check whether the training set is balanced, that is,
# having the same number of positive and negative samples.
print('Number of training samples: ', len(y_train))
print('Number of positive samples: ', sum(y_train))
print('Number of test samples: ', len(y_test))

# Print a training sample
print(X_train[0])

word_index = imdb.get_word_index()
index_word = {index: word for word, index in word_index.items()}
print([index_word.get(i, ' ') for i in X_train[0]])

review_length = [len(x) for x in X_train]

plt.hist(x=review_length, bins=10)
plt.show()

max_length = 200
X_train = pad_sequences(X_train, maxlen=max_length)
X_test = pad_sequences(X_test, maxlen=max_length)

print('X_train shape after padding: ', X_train.shape)
print('X_test shape after padding: ', X_test.shape)

tf.random.set_seed(42)
model = models.Sequential([layers.Embedding(input_dim=5000, output_dim=32),
                           layers.LSTM(units=50),
                           layers.Dense(units=1, activation='sigmoid')])

print(model.summary())
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=X_train, y=y_train, batch_size=64, epochs=3, validation_data=(X_test, y_test))

accuracy = model.evaluate(x=X_test, y=y_test, verbose=0)[1]
print('Test accuracy: ', accuracy)

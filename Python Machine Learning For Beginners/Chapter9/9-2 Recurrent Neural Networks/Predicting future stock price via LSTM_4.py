import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Activation, Dense, Flatten, Dropout, LSTM
from tensorflow.keras.models import Model

fb_complete_data = pd.read_csv('FB _train.csv')
print(fb_complete_data)

fb_training_processed = fb_complete_data['Open']
print(fb_training_processed)

fb_training_processed = fb_training_processed.values
print(fb_training_processed)

scaler = MinMaxScaler(feature_range=(0, 1))

fb_training_processed = fb_training_processed.reshape((-1, 1))

fb_training_scaled = scaler.fit_transform(X=fb_training_processed)
print(len(fb_training_scaled))

# Training feature set contains the opening stock price of the past 60 days.
fb_training_feature_set = []
for i in range(60, len(fb_training_scaled)):
    fb_training_feature_set.append(fb_training_scaled[i - 60:i, 0])

fb_training_label_set = []
for i in range(60, len(fb_training_scaled)):
    fb_training_label_set.append(fb_training_scaled[i, 0])

# We need to convert our data into Numpy array before we can use as input with Keras.
X_train = np.array(fb_training_feature_set)
y_train = np.array(fb_training_label_set)

print(X_train.shape)
print(y_train.shape)

# We need to reshape our input features into 3-dimensional format.
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Defining the LSTM network

input_layer = Input(shape=(X_train.shape[1], 1))
LSTM1 = LSTM(units=100, activation='relu', return_sequences=True)(input_layer)
drop1 = Dropout(0.2)(LSTM1)
LSTM2 = LSTM(units=100, activation='relu', return_sequences=True)(drop1)
drop2 = Dropout(0.2)(LSTM2)
LSTM3 = LSTM(units=100, activation='relu', return_sequences=True)(drop2)
drop3 = Dropout(0.2)(LSTM3)
LSTM4 = LSTM(units=100, activation='relu')(drop3)
drop4 = Dropout(0.2)(LSTM4)
output_layer = Dense(1)(drop4)

model = Model(input_layer, output_layer)

model.compile(optimizer='adam', loss='mse')

print(X_train.shape)
print(y_train.shape)

y_train = y_train.reshape(-1, 1)
print(y_train.shape)

# Train our stock price prediction model on the training set.
model_history = model.fit(x=X_train, y=y_train, epochs=100, verbose=1, batch_size=32,
                          validation_split=0.2)

fb_testing_complete_data = pd.read_csv('FB_test.csv')

fb_testing_processed = fb_testing_complete_data[['Open']].values

fb_all_data = pd.concat((fb_complete_data['Open'], fb_testing_complete_data['Open']), axis=0)

test_inputs = fb_all_data[len(fb_all_data) - len(fb_testing_complete_data) - 60:].values

print(test_inputs.shape)

test_inputs = test_inputs.reshape(-1, 1)
test_inputs = scaler.transform(X=test_inputs)

print(test_inputs.shape)

fb_test_feature_set = []
for i in range(60, 80):
    fb_test_feature_set.append(test_inputs[i - 60: i, 0])


X_test = np.array(fb_test_feature_set)
print(X_test.shape)

# Converting test data into 3D shape
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

print(X_test.shape)

# Making predictions on test set
y_prediction = model.predict(x=X_test)

# Converting scaled data back to original data
y_prediction = scaler.inverse_transform(y_prediction)

plt.figure(figsize=(8, 6))
plt.plot(fb_testing_processed, color='red', label='Actual Facebook Stock Price')
plt.plot(y_prediction, color='green', label='Predicted Facebook Stock Price')
plt.title('Facebook Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()

plt.savefig('Stock price trajectory.jpg')

plt.show()

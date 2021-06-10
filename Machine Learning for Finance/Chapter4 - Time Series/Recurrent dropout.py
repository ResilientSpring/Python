from tensorflow.keras.layers import Dense, Flatten, SimpleRNN, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import mean_absolute_percentage_error
import Conv1D_2 as eyes_meet

number_of_features = 29
max_length = 100

model = Sequential([LSTM(units=16, recurrent_dropout=0.1, return_sequences=True,
                         input_shape=(max_length, number_of_features)),
                    LSTM(units=16, recurrent_droput=0.1),
                    Dense(units=1)])

model.compile(optimizer='adam', loss=mean_absolute_percentage_error)

model.fit_generator(eyes_meet.train_gen, epochs=1,
                    steps_per_epoch=eyes_meet.n_train_samples // eyes_meet.batch_size,
                    validation_data=eyes_meet.val_gen,
                    validation_steps=eyes_meet.n_train_samples // eyes_meet.batch_size)

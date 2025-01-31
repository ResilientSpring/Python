from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import mean_absolute_percentage_error

model = Sequential([SimpleRNN(units=16, return_sequences=True, input_shape=[max_length, n_features]),
                    SimpleRNN(units=32, return_sequences=True),
                    SimpleRNN(units=64),
                    Dense(units=1)])

model.compile(optimizer='adam', loss=mean_absolute_percentage_error)

model.fit_generator(generator=train_generator, epochs=20,
                    steps_per_epoch=n_train_samples // batch_size,
                    validation_data=val_gen, validation_steps=n_val_samples // batch_size)

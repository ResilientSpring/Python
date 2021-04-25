from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation
import Densely_Connected_Neural_Network as DNN
from keras.optimizers import Adam

def create_model(learning_rate=0.001, dropout_rate=0.1):

    '''Create sequential model'''
    model = Sequential()

    # Adding dense layers
    model.add(Dense(units=12, input_dim=DNN.X_train.shape[1], activation="relu"))
    model.add(Dropout(rate=dropout_rate))
    model.add(Dense(units=6, activation="relu"))
    model.add(Dropout(rate=dropout_rate))
    model.add(Dense(units=1, activation="sigmoid"))

    # Compiling the model
    adam = Adam(lr=learning_rate)
    model.compile(optimizer=adam, metrics=["accuracy"], loss="binary_crossentropy")

    return model


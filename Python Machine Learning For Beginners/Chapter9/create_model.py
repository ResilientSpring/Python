from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation
import Densely_Connected_Neural_Network as DNN

def create_model(learning_rate, dropout_rate):

    '''Create sequential model'''
    model = Sequential()

    # Adding dense layers
    model.add(Dense(units=12, input_dim=DNN.X_train.shape[1], activation="relu"))


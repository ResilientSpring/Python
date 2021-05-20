from keras.models import Sequential
from keras.layers import Dense, Dropout

# 50% of nodes randomly picked from the 32-node layer are ignored in an iteration during training.

model = Sequential(layers=[Dense(units=32, activation='relu'),
                           Dropout(rate=0.5),
                           Dense(units=1)])


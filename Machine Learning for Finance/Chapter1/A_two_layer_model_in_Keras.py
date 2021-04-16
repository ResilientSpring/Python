from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout

# Building a neural network in the sequential API works as follows.

## Firstly, we create an empty sequential model with no layers:
model = Sequential();

## Then we can add layers to this model, just like stacking a layer cake, with model.add().

## For the first layer, we have to specify the input dimensions of the layer.
### Two features (the coordinates of the point)
model.add(Dense(units=3, input_dim=2));

## Add a tanh activation function:
model.add(Activation("tanh"));

## Add the linear step and the activation function of the output layer:
model.add(Dense(1));
model.add(Activation("sigmoid"));

## Get an overview of all the layers:
print(model.summary());
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# In this example, you know that the relationship between the numbers is Y=3X+1.[1]
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Initialize the simplest possible neural network (model).
# It has one layer, that layer has one neuron, and the input shape to it is only one value.[1]
model = Sequential([Dense(units=1, input_shape=[1])])

# When the computer is trying to learn that, it makes a guess, maybe Y=10X+10.
# The loss function measures the guessed answers against the known correct answers
# and measures how well or badly it did.[1]
model.compile(optimizer='sgd', loss='mean_squared_error')
# Next, the model uses the optimizer function to make another guess.
# Based on the loss function's result, it tries to minimize the loss.
# At this point, maybe it will come up with something like Y=5X+5.
# While that's still pretty bad, it's closer to the correct result (the loss is lower).

# Train it to see if it can infer the relationship (patterns) between
# those numbers in X and Y, and use them to create a model.
# The process of training the neural network, where it learns the relationship between
# the X's and Y's, is in the model.fit call. That's where it will go through the loop before
# making a guess, measuring how good or bad it is (the loss), or
# using the optimizer to make another guess.
# It will do that for the number of epochs that you specify.
# When you run that code, you'll see the loss will be printed out for each epoch.[2]
model.fit(xs, ys, epochs=500)
# The model repeats that for the number of epochs


# By the time the training is done, the loss is extremely small, showing that our model is doing
# a great job of inferring the relationship between the numbers.

# You probably don't need all 500 epochs and can experiment with different amounts.
# As you can see from the example, the loss is really small after only 50 epochs,
# so that might be enough![2]


# You have a model that has been trained to learn the relationship between X and Y.
# You can use the model.predict method to have it figure out the Y for a previously unknown X.

# For example, if X is 10, what do you think Y will be? Take a guess before you run the following
# code:
print(model.predict(x=[10]))
print(model.predict(x=[10.0]))

# You might have thought 31, but it ended up being a little over. Why do you think that is?
#
# Neural networks deal with probabilities, so it calculated that there is a very high probability
# that the relationship between X and Y is Y=3X+1, but it can't know for sure with only six data
# points. The result is very close to 31, but not necessarily 31.
#
# As you work with neural networks, you'll see that pattern recurring.
# You will almost always deal with probabilities, not certainties,
# and will do a little bit of coding to figure out what the result is based on the probabilities,
# particularly when it comes to classification.[3]

# Reference:
# 1. https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F#2
# 2. https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F#3
# 3. https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F#4

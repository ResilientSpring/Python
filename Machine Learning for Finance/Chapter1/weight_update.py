# Activation function

def activation_function(dW, dBias, Weight, Bias, learning_rate=1):
    Weight -= learning_rate * dW;
    Bias -= learning_rate * dBias;

    return [Weight, Bias];
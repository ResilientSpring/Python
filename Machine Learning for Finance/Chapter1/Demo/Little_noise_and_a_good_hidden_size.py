import numpy as np
import Hidden_layer_size as h
import matplotlib.pyplot as plt
import sklearn

# Generate a dataset and plot it
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.15)
y = y.reshape(200, 1)
plt.scatter(X[:, 0], X[:, 1], s=40, c=y.flatten(), cmap=plt.cm.Spectral)

# Hyper parameters
hiden_layer_size = 3
# I picked this value because it showed good results in my experiments
learning_rate = 0.01

# Initialize the parameters to random values. We need to learn these.
np.random.seed(0)
# This is what we return at the end
model = h.initialize_parameters(nn_input_dim=2, nn_hdim=hiden_layer_size, nn_output_dim=1)
model = h.train(model, X, y, learning_rate=learning_rate, num_passes=1000, print_loss=True)

# Plot the decision boundary
h.plot_decision_boundary(lambda x: h.predict(model, x))
plt.title("Decision Boundary for hidden layer size 3")

plt.savefig("Little_noise_and_a_good_hidden_size.jpg");

plt.show();

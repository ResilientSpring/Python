from keras.datasets import fashion_mnist

fashion_mnist = fashion_mnist

(train_images, train_labels), (test_imanges, test_labels) = fashion_mnist.load_data()

# Print a few samples from these four arrays, for example, the training labels as follows:
print(train_labels)

# The label arrays do not include class names. Hence, we define them as follows and will
# use them for plotting later on:

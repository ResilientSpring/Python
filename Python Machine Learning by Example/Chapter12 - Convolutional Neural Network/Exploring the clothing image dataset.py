from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt

fashion_mnist = fashion_mnist

(train_images, train_labels), (test_imanges, test_labels) = fashion_mnist.load_data()

# Print a few samples from these four arrays, for example, the training labels as follows:
print(train_labels)

# The label arrays do not include class names. Hence, we define them as follows and will
# use them for plotting later on:
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
               'Sneaker', 'Bag', 'Ankle boot']

# Take a look at the format of the image
print(train_images.shape)

# Similarly for the 10000 testing samples, we check the format as follows:
print(test_imanges.shape)

# Let's now inspect a random training sample
plt.figure()
plt.imshow(train_images[42])
plt.colorbar()
plt.grid(False)
plt.title(class_names[train_labels[42]])

plt.savefig('Fashion_MNIST.jpg')

plt.show()

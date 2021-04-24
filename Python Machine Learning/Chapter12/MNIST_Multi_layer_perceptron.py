import load_mnist as loader
import matplotlib.pyplot as plt

X_train, y_train = loader.load_mnist('', kind="train")
print("Rows: {:d}, columns: {:d}".format(X_train.shape[0], X_train.shape[1]))

X_test, y_test = loader.load_mnist('', kind='t10k')
print("Rows: {:d}, columns: {:d}".format(X_test.shape[0], X_test.shape[1]))

fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)

ax = ax.flatten()

# let's visualize examples of the digits 0-9
for i in range(10):

    # Reshape the 784-pixel vectors from our feature matrix into the original 28 x 28 image
    img = X_train[y_train == i][0].reshape(28, 28)

    ax[i].imshow(img, cmap="Greys")


ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()

plt.savefig("Visualization of MNIST examples of digits 0-9.jpg")

plt.show()
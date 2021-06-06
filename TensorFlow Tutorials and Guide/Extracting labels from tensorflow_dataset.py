import tensorflow_datasets as tfds

ds = tfds.load('cifar10', split='train', as_supervised=True)
ds = ds.take(1)

for image, label in tfds.as_numpy(ds):
    print(type(image), type(label), label)


# Reference:
# https://www.tensorflow.org/datasets/overview#as_numpy_tfdsas_numpy
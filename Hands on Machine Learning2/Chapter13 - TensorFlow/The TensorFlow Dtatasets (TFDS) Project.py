import tensorflow_datasets as tfds

dataset = tfds.load(name='cifar10')

print(dataset)

# Image, label = dataset['image'], dataset['label']

# You can then apply any transformation you want (typically shuffling, batching, and prefetching),
# and you're ready to train your model.

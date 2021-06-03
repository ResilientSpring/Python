import tensorflow_datasets as tfds

dataset = tfds.load(name='cifar10')

print(dataset)

cifar10_train, cifar10_test = dataset['train'], dataset['test']

# You can then apply any transformation you want (typically shuffling, batching, and prefetching),
# and you're ready to train your model.
cifar10_train = cifar10_train.batch(128)
cifar10_train = cifar10_train.map(lambda items : (items['image'], items['label']))
cifar10_train = cifar10_train.prefetch(1)

for images, labels in cifar10_train.take(1):
    print(images.shape)
    print(labels.numpy())


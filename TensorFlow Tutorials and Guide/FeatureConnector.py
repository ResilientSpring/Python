import tensorflow_datasets as tfds
import tensorflow as tf

tfds.core.DatasetInfo(
    features=tfds.features.FeaturesDict({
        'image': tfds.features.Image(shape=(28, 28, 1)),
        'label': tfds.features.ClassLabel(names=['no', 'yes']),
        'metadata': {
            'id': tf.int64,
            'language': tf.string,
        },
    }),
)

(ds_train, ds_test), ds_info = tfds.load(
    name='cifar10',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

# Reference:
# 1. https://www.tensorflow.org/datasets/features
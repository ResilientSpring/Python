import tensorflow_datasets as tfds
import tensorflow as tf

@tfds.decode.make_decoder()
def decode_example(serialized_image, feature):
    crop_y, crop_x, crop_height, crop_width = 10, 10, 64, 64
    return tf.image.decode_and_crop_jpeg(
        serialized_image,
        [crop_y, crop_x, crop_height, crop_width],
        channels=feature.feature.shape[-1],
    )
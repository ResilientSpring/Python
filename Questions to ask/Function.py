import tensorflow as tf

def preprocessing(path, label):

    image_loaded_for_preprocessing = tf.io.read_file(filename=path)

    decoded_image = tf.image.decode_image(contents=image_loaded_for_preprocessing, channels=3)

    image = tf.image.resize(images=decoded_image, size=[image_height, image_width]) # How can image_height and image_width be declared first

    image = image / 255.0

    return image, label

image_height, image_width = 120, 80 # and initialized later?


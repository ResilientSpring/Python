import tensorflow as tf

# You can easily create a TFRecord file using the tf.io.TFRecordWriter
with tf.io.TFRecordWriter("my_data.tfrecord") as f:
    f.write(b'This is the first record.')
    f.write(b'And this is the second record.')


# You can then use a tf.data.TFRecordDataset to read one or more TFRecord files:
filepaths = ["my_data.tfrecord"]

dataset = tf.data.TFRecordDataset(filepaths)

for item in dataset:
    print(item)


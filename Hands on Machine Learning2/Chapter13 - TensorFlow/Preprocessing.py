import Building_an_input_pipeline as input_pipeline
import tensorflow as tf
import Split_the_California_dataset_to_multiple_CSV_files as chunks

n_inputs = 8 # X_train.shape[-1]

@tf.function
def preprocess(line):
    defs = [0.] * n_inputs + [tf.constant([], dtype=tf.float32)]
    fields = tf.io.decode_csv(records=line, record_defaults=input_pipeline.record_defaults)

    x = tf.stack(values=fields[:-1])
    y = tf.stack(values=fields[-1:])

    return (x - chunks.X_mean) / chunks.X_std, y


value = preprocess(b'4.2083, 44.0, 5.3232, 0.9171, 846.0, 2.3370, 37.47, -122.2, 2.782')

print(value)
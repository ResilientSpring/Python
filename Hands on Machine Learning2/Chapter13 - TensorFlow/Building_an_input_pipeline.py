import Split_the_California_dataset_to_multiple_CSV_files as spliter
import tensorflow as tf

filepath_dataset = tf.data.Dataset.list_files(file_pattern=spliter.train_filepaths, seed=42)

for filepath in filepath_dataset:
    print(filepath)



n_readers = 5
dataset = filepath_dataset.interleave(lambda filepath: tf.data.TextLineDataset(filepath).skip(1),
                                      cycle_length=n_readers)

for line in dataset.take(5):
    print(line.numpy())



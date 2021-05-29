import pickle
import tensorflow as tf

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')

    return dict


train_filepath = ["data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4", "data_batch_5"]

filepath_dataset = tf.data.Dataset.list_files(file_pattern=train_filepath, seed=42)

for filepath in filepath_dataset:
    print(filepath)

data = unpickle(train_filepath)

print(data["data"].shape)



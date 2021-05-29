import pickle
import tensorflow as tf

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')

    return dict


data_batch_1 = unpickle("data_batch_1")

print(data_batch_1["data"])

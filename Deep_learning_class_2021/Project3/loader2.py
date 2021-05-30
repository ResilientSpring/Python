import pickle
import tensorflow as tf

def unpickle(file):
    with open(file, 'rb') as file_output:
        dict = pickle.load(file_output, encoding='bytes')

    return dict


data_batch_1 = unpickle("data_batch_1")

print(type(data_batch_1))

print(data_batch_1.keys())

import tensorflow as tf
import numpy as np
import pandas as pd

train_filepath = ["data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4", "data_batch_5"]

filepath_dataset = tf.data.Dataset.list_files(file_pattern=train_filepath, seed=42)

for filepath in filepath_dataset:
    print(filepath)



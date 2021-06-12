from tensorflow.keras.layers import Embedding
import tensorflow as tf
from tensorflow.keras.models import Sequential

model = Sequential([Embedding(input_dim=100, output_dim=6, input_length=20, name='embed-layer')])

model.summary()

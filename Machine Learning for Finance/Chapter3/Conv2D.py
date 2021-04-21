from keras.layers import Conv2D
from keras.models import Sequential

model = Sequential()

img_shape = (28, 28, 1)
model.add(Conv2D(filters=6, kernel_size=3, strides=1, padding='valid', input_shape=img_shape))
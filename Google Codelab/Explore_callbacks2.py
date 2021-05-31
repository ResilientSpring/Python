import tensorflow as tf
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

# Earlier, when you trained for extra epochs, you had an issue where your loss might change.
# It might have taken a bit of time for you to wait for the training to do that and you might
# have thought that it would be nice if you could stop the training when you reach a desired value,
# such as 95% accuracy. If you reach that after 3 epochs, why sit around waiting for it to finish
# a lot more epochs?
# Like any other program, you have callbacks!

class myCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        if(logs.get('accuracy') > 0.95):
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True


callbacks = myCallback()

mnist = fashion_mnist

(training_images, training_labels), (test_imanges, test_labels) = mnist.load_data()

training_images = training_images / 255.0
test_images = test_imanges / 255.0

model = Sequential([Flatten(),
                    Dense(units=512, activation=tf.nn.relu),
                    Dense(units=10, activation=tf.nn.softmax)])


model.compile(optimizer='adam', loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])

history = model.fit(x=training_images, y=training_labels, epochs=50, callbacks=[callbacks])


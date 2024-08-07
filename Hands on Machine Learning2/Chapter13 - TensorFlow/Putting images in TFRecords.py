from sklearn.datasets import load_sample_images
import matplotlib.pyplot as plt
import tensorflow as tf

img = load_sample_images()['images'][0]
plt.imshow(img)
plt.axis('off')
plt.title('Original Image')

plt.savefig('TFRecords.jpg')

plt.show()

data = tf.io.encode_jpeg(img)

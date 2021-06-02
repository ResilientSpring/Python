import os.path
import pathlib
import matplotlib.pyplot as plt
import tensorflow as tf

# Use the pathlib library to generate a list of image files:
image_directory_path = pathlib.Path('cat_dog_images')

# The glob module finds all the pathnames matching a specified pattern according to the rules used.[2]
for path in image_directory_path.glob('*.jpg'):
    print(path)

list_of_image_paths = [str(path) for path in image_directory_path.glob('*.jpg')]
print(list_of_image_paths)

labels = [1 if 'dog' in os.path.basename(image) else 0
          for image in list_of_image_paths]

print(labels)

dataset_of_image_and_label = tf.data.Dataset.from_tensor_slices((list_of_image_paths, labels))

for item in dataset_of_image_and_label:
    print('X:', item[0].numpy(), 'y:', item[1].numpy())

def load_and_preprocess(path, label):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [img_height, img_width])
    image = image / 255.0

    return image, label


img_width, img_height = 120, 80

dataset_of_processed_image_and_label = dataset_of_image_and_label.map(load_and_preprocess)

figure = plt.figure(figsize=(10, 5))

for i, example in enumerate(dataset_of_processed_image_and_label):
    print(example[0].shape, example[1].numpy())
    ax = figure.add_subplot(2, 3, i + 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(example[0])
    ax.set_title('{}'.format(example[1].numpy()), size=15)

plt.tight_layout()
plt.show()

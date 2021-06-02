import os.path
import pathlib
import tensorflow as tf
import matplotlib.pyplot as plt

# Use the pathlib library to generate a list of image files:
image_directory_path = pathlib.Path('cat_dog_images')

# sorted(iterable sequence to sort, key=key, reverse=reverse)
file_path_list = sorted([str(path) for path in image_directory_path.glob('*.jpg')])

print(file_path_list)

# Ground truths for these images can be found within their file paths.
# So, we extract these labels from the list of their file paths,
numeric_list_of_labels = [1 if 'dog' in os.path.basename(file) else 0 for file in file_path_list]
#                       [For file in file_path_list, 1 if 'dog' in os.path.basename(file) else 0]

print(numeric_list_of_labels)  # Now we have a list of their labels.

# Creating a joint dataset from two lists.
dataset_of_files_and_labels = tf.data.Dataset.from_tensor_slices((numeric_list_of_labels,
                                                                  file_path_list))

for individual_dataset in dataset_of_files_and_labels:
    print('X:', individual_dataset[1].numpy(), 'y:', individual_dataset[0].numpy())


def preprocessing(path, label):

    image_loaded_for_preprocessing = tf.io.read_file(filename=path)

    decoded_image = tf.image.decode_image(contents=image_loaded_for_preprocessing, channels=3)

    image = tf.image.resize(images=decoded_image, size=[image_height, image_width])

    image = image / 255.0

    return image, label

image_height, image_width = 120, 80

dataset_of_images_labels_bond = dataset_of_files_and_labels.map(preprocessing)

figure = plt.figure(figsize=(10, 6))

for i, example in enumerate(dataset_of_images_labels_bond):
    ax = figure.add_subplot(2, 3, i + 1)
    ax.set_xticks([]); ax.set_yticks([])

    ax.imshow(example[0])

    ax.set_title('{}'.format(example[1].numpy()), size=15)

plt.tight_layout()

plt.savefig('Preprocessed images.jpg')
plt.show()



import os.path
import pathlib
import matplotlib.pyplot as plt
import tensorflow as tf

# Use the pathlib library to generate a list of image files:
image_directory_path = pathlib.Path('cat_dog_images')

for path in image_directory_path.glob('*.jpg'):
    print(path)

list = [str(path) for path in image_directory_path.glob('*.jpg')]
print(list)

# sorted(iterable sequence to sort, key=key, reverse=reverse) [1]
file_list = sorted(list)

print(file_list)

# Next, we will visualize these image examples using Matplotlib:
fig = plt.figure(figsize=(10, 5))

for i, file in enumerate(file_list):

    img_raw = tf.io.read_file(file)

    img = tf.image.decode_image(contents=img_raw)

    print('Image shape:', img.shape)

    ax = fig.add_subplot(2, 3, i+1)
    ax.set_xticks([]); ax.set_yticks([])
    ax.imshow(img)

    ax.set_title(os.path.basename(file), size=15)

plt.savefig('ch3-catdog-example.jpg')
plt.tight_layout()
plt.show()

# References:
# 1. https://www.w3schools.com/python/ref_func_sorted.asp
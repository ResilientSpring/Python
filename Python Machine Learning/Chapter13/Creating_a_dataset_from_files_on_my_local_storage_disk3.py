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
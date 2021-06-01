import pathlib

# Use the pathlib library to generate a list of image files:
image_directory_path = pathlib.Path('cat_dog_images')

# sorted(iterable sequence to sort, key=key, reverse=reverse)
file_list = sorted([str(path) for path in image_directory_path.glob('*.jpg')])

print(file_list)

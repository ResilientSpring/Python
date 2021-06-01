import pathlib

# Use the pathlib library to generate a list of image files:
image_directory_path = pathlib.Path('cat_dog_images')

for path in image_directory_path.glob('*.jpg'):
    print(path)

list = [str(path) for path in image_directory_path.glob('*.jpg')]
print(list)

# sorted(iterable sequence to sort, key=key, reverse=reverse) [1]
file_list = sorted(list)

print(file_list)

# References:
# 1. https://www.w3schools.com/python/ref_func_sorted.asp
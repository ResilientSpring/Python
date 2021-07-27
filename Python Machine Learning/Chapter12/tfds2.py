import tensorflow_datasets as tfds

celebrity = tfds.load('celeb_a', with_info=True, shuffle_files=False)
print(celebrity)

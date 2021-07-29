import tensorflow_datasets as tfds

celebrity, celebrity_info = tfds.load('celeb_a', with_info=True, shuffle_files=False)
print(celebrity_info)
print(celebrity.keys())
print(celebrity.values())
print(celebrity.items())

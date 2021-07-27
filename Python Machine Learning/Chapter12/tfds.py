import tensorflow_datasets as tfds

celebrity, celebrity_info = tfds.load('celeb_a', with_info=True, shuffle_files=False)
print(celebrity_info)

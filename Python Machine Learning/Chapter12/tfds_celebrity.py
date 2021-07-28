import tensorflow_datasets as tfds

celebrity, celebrity_info = tfds.load(name='celeb_a', with_info=True, )
print(celebrity_info)

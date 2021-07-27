import tensorflow_datasets as tfds

celebrity = tfds.load('celeb_a', with_info=True, shuffle_files=False)
print(celebrity)

print('='*30)

celebrity2 = tfds.load(name='celeb_a')
print(celebrity2)

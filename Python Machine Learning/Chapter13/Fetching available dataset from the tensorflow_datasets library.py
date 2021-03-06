import tensorflow_datasets as tfds

print(len(tfds.list_builders()))

# Print the first five datasets
print(tfds.list_builders()[:5])

# Print all dataset as of now:
print(tfds.list_builders())

# Fetch a dataset
celeba_bldr = tfds.builder("celeb_a")

print('\n', 30*"=", '\n')

print(celeba_bldr.info.features.keys())

print('\n', 30*"=", '\n')

print(celeba_bldr.info.features['image'])

print('\n', 30*"=", '\n')

print(celeba_bldr.info.features['attributes'].keys())

print('\n', 30*"=", '\n')

print(celeba_bldr.info.features['landmarks'].keys())

print('\n', 30*"=", '\n')

print(celeba_bldr.info.citation)

# Download the dataset and store it in a designated folder for all TensorFlow dataset on local disk.
celeba_bldr.download_and_prepare()

# Next, we will instantiate the dataset as follows:
datasets = celeba_bldr.as_dataset(shuffle_files=False)

print(datasets.keys())

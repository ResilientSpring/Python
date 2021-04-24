import tensorflow as tfds

iris, iris_info = tfds.load("iris", with_info=True)
print(iris_info)
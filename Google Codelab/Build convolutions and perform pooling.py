#  Deep Neural Network (DNN) for computer vision might not be useful because it requires
#  the target to be the only thing in the picture, and it has to be centered.

# Of course, this isn't a realistic scenario. You will want your DNN to be able to
# identify the target in pictures with other objects or where it isn't positioned front and center.
# To do this, you'll need convolutions.

# The padding parameter in convolutional layers can have two values:
# "same": pad with zeros so as to produce outputs of the same width/height as the input
# "valid": no padding, only use real pixels.
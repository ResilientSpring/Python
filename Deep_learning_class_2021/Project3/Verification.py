# Import hashlib library (md5 method is part of it)
import hashlib

# The file to check
file_name = "data_batch_1"

# Correct original md5 goes here
original_md5 = 'c58f30108f718f92721af3b95e74349a'

# Open, close, read file and calculate MD5 on its contents
with open(file_name) as file_to_check:

    # read contents of the file
    data = file_to_check.read()

    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()


# Finally compare original MD5 with freshly calculated
if original_md5 == md5_returned:
    print('MD5 verified.')
else:
    print('MD5 verification failed.')


# Reference: https://stackoverflow.com/a/16876405/14900011
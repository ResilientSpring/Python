import hashlib

file_name_list = ["data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4", "data_batch_5"]

with open("data_batch_1" + "data_batch_2" + "data_batch_3" + "data_batch_4" + "data_batch_5", 'rb') \
        as file_to_check:
    file_hash = hashlib.md5()

    for chunk in iter(lambda : file_to_check.read(n=8192), b""):
        file_hash.update(chunk)

#        return file_hash.hexdigest()

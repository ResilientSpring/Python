import hashlib

def file_as_bytes(file):
    with file:
        return file.read()


file_name_list = ["data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4", "data_batch_5"]

print([(file_name, hashlib.md5(file_as_bytes(open(file_name, 'rb'))).digest()) for file_name in
       file_name_list])

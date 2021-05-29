import hashlib

def md5(file_name):
    hash_md5 = hashlib.md5()

    with open(file_name, "rb") as file_to_check:
        for chunk in iter(lambda : file_to_check.read(n=4096), b""):
            hash_md5.update(chunk)

            return hash_md5.hexdigest()


a_list_of_file = ["data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4", "data_batch_5"]

print(md5(a_list_of_file))

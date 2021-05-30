import zlib

def adler32sum(filename, blocksize=65536):
    check_sum = zlib.adler32("")
    with open(filename, 'rb') as file_to_check:
        for block in iter(lambda : file_to_check.read(blocksize), b""):
            check_sum = zlib.adler32(block, check_sum)

    return check_sum & 0xffffffff



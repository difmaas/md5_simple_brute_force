import hashlib
def crack(hash):
    plain_text = '00001'
    plain_text_len = len(plain_text)
    for i in range(99999):
        plain_text = int(plain_text) + 1
        # add zero fill in the front of number as long plain text length
        plain_text = str(plain_text).zfill(plain_text_len)
        hash_text = hashlib.md5(plain_text.encode())
        if hash_text.hexdigest() == hash:
            return plain_text 
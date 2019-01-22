# built-in hash lib
import hashlib

from cryptography.fernet import Fernet

# print(hashlib.algorithms_available)

hash_obj = hashlib.sha3_256()

# b - byte string Hello
hash_obj.update(b"Hello")

print(hash_obj.hexdigest())

key = Fernet.generate_key()
cipher = Fernet(key)
print(cipher.encrypt(b"Hello"))

# Message can be descrypted using the key

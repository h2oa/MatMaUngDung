import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Thư viện pycrypto
from Crypto.Cipher import AES as AES_pycrypto
# Thư viện pycryptodome
from Crypto.Cipher import AES as AES_pycryptodome

# data so sánh, với độ dài 16 x 10000
data = b'lengochoa 200234' * 10000

key = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
iv = os.urandom(16)

# Sử dụng pycrypto
start_time = time.time()
cipher = AES_pycrypto.new(key, AES_pycrypto.MODE_CBC, iv)
encrypted_data = cipher.encrypt(pad(data, AES.block_size))
elapsed_time = time.time() - start_time
print(f"pycrypto Encryption Time: {elapsed_time:.6f} seconds")

# Sử dụng pycryptodome
start_time = time.time()
cipher = AES_pycryptodome.new(key, AES_pycryptodome.MODE_CBC, iv)
encrypted_data = cipher.encrypt(pad(data, AES.block_size))
elapsed_time = time.time() - start_time
print(f"pycryptodome Encryption Time: {elapsed_time:.6f} seconds")

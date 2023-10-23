from Crypto.Cipher import AES
import os

KEY = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'

# encrypt and return a hex encode ciphertext
def encrypt(plaintext):
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(plaintext.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return ciphertext

# decrypt with ciphertext in hex encode
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

plaintext = 'lengochoa 200234'
ciphertext = encrypt(plaintext)
print(ciphertext)
print(decrypt(ciphertext))
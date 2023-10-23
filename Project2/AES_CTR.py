from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
import json

KEY = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'

# encrypt and return a json object with hex encode
def encrypt(plaintext):

    cipher = AES.new(KEY, AES.MODE_CTR)
    encrypted = cipher.encrypt(plaintext.encode())
    nonce = hex(bytes_to_long(cipher.nonce))
    ciphertext = hex(bytes_to_long(encrypted))

    return json.dumps({'nonce': nonce, 'ciphertext': ciphertext})

# decrypt with json_data in hex encode
def decrypt(json_data):
    data = json.loads(json_data)
    nonce = bytes.fromhex(data['nonce'][2:])
    ciphertext = bytes.fromhex(data['ciphertext'][2:])
    
    cipher = AES.new(KEY, AES.MODE_CTR, nonce = nonce)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

plaintext = 'lengochoa 200234'
json_data = encrypt(plaintext)
print(json_data)
print(decrypt(json_data))
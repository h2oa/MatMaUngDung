from Crypto.Cipher import AES

key = "36f18357be4dbd77f050515c73fcf9f2"
key = bytes.fromhex(key)
ciphertext = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"

nonce = bytes.fromhex(ciphertext[:30])
counter = bytes.fromhex(ciphertext[30:32])
ciphertext = bytes.fromhex(ciphertext[32:])
cipher = AES.new(key, AES.MODE_CTR, nonce = nonce, initial_value = counter)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
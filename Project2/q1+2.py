from Crypto.Cipher import AES

key = "140b41b22a29beb4061bda66b6747e14"
key = bytes.fromhex(key)
ciphertext = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
ciphertext = bytes.fromhex(ciphertext)

iv = ciphertext[:16]
ciphertext = ciphertext[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
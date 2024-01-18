#pip install cryptography

from cryptography.fernet import Fernet

with open('key.txt', 'rb') as key_to_open:
    key = key_to_open.read()

with open('encrypted.bak', 'rb') as file:
    encrypted = file.read()

eq = Fernet(key)

decrypt = eq.decrypt(encrypted)

with open('decrypted.bak', 'wb') as file:
    file.write(decrypt)

print('Data dencrypted sucessfully!')
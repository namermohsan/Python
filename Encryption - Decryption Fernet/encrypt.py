# pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key.txt', 'wb') as file:
    file.write(key)

with open('key.txt', 'rb') as file:
    key = file.read()

with open('database.bak', 'rb') as file:
    database = file.read()

eq = Fernet(key)
encrypted = eq.encrypt(database)

with open('encrypted.bak', 'wb') as file:
    file.write(encrypted)

# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_file(key, file_path):
    chunk_size = 64 * 1024
    output_file = file_path + ".enc"
    file_size = str(os.path.getsize(file_path)).zfill(16)
    IV = get_random_bytes(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(file_path, 'rb') as input_file:
        with open(output_file, 'wb') as output:
            output.write(file_size.encode('utf-8'))
            output.write(IV)

            while True:
                chunk = input_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                output.write(encryptor.encrypt(chunk))

    # os.remove(file_path)
    with open('new_key.txt', 'wb') as file:
        file.write(key)

# Example usage
key = get_random_bytes(16)  # Generate a 16-byte key
file_path = "decrypted.bak"
encrypt_file(key, file_path)
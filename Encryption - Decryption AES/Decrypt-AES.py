from Crypto.Cipher import AES
import os

def decrypt_file(key, file_path):
    chunk_size = 64 * 1024
    output_file = "decrypted_" + file_path

    with open(file_path, 'rb') as input_file:
        file_size = int(input_file.read(16))
        IV = input_file.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(output_file, 'wb') as output:
            while True:
                chunk = input_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                output.write(decryptor.decrypt(chunk))

            output.truncate(file_size)

# Example usage
with open('new_key.txt', 'rb') as file:
    key = file.read() # Use the same key used for encryption
file_path = "enc.bak"
decrypt_file(key, file_path)
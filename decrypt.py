import os
import pyaes

class Decrypter:
    def __init__(self, encrypted_file_name, key):
        self.encrypted_file_name = encrypted_file_name
        self.key = key

    def decrypt(self):
        # Abrir o arquivo criptografado
        with open(self.encrypted_file_name, "rb") as file:
            file_data = file.read()
        
        # Descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(self.key)
        decrypt_data = aes.decrypt(file_data)
        
        # Remover o arquivo criptografado
        os.remove(self.encrypted_file_name)
        
        # Criar o arquivo descriptografado
        original_file_name = self.encrypted_file_name.replace(".ransomwaretroll", "")
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)
        
        return original_file_name

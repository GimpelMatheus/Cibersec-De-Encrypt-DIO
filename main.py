import os
import random
import string
from encrypt import Encrypter
from decrypt import Decrypter


def create_test_files(folder="arquivos_teste", num_files=50):
    """Cria arquivos de teste com conteúdo aleatório."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for i in range(1, num_files + 1):
        file_name = os.path.join(folder, f"teste_{i}.txt")
        # Não recria o arquivo se ele já existir
        if not os.path.exists(file_name):
            content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
            with open(file_name, "w") as file:
                file.write(content)
    print(f"{num_files} arquivos de teste criados ou já existentes em '{folder}'.")


def encrypt_files(input_folder, output_folder, key):
    """Criptografa todos os arquivos de uma pasta e salva em outra."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        full_path = os.path.join(input_folder, file_name)
        if os.path.isfile(full_path):
            encrypter = Encrypter(full_path, key)
            encrypted_file = encrypter.encrypt()
            # Salva no destino sem remover arquivos originais
            new_file_path = os.path.join(output_folder, os.path.basename(encrypted_file))
            if not os.path.exists(new_file_path):
                os.rename(encrypted_file, new_file_path)
            print(f"Arquivo criptografado salvo em: {new_file_path}")


def decrypt_files(input_folder, output_folder, key):
    """Descriptografa todos os arquivos de uma pasta e salva em outra."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        full_path = os.path.join(input_folder, file_name)
        if os.path.isfile(full_path):
            decrypter = Decrypter(full_path, key)
            decrypted_file = decrypter.decrypt()
            # Salva no destino sem remover arquivos originais
            new_file_path = os.path.join(output_folder, os.path.basename(decrypted_file))
            if not os.path.exists(new_file_path):
                os.rename(decrypted_file, new_file_path)
            print(f"Arquivo descriptografado salvo em: {new_file_path}")


def main():
    # Definir pastas
    test_folder = "arquivos_teste"
    encrypted_folder = "arquivos_criptografados"
    decrypted_folder = "arquivos_descriptografados"
    key = b"testeransomwares"

    # Etapas do processo
    print("1. Gerando arquivos de teste...")
    create_test_files(test_folder)

    print("\n2. Criptografando arquivos de teste...")
    encrypt_files(test_folder, encrypted_folder, key)

    print("\n3. Descriptografando arquivos criptografados...")
    decrypt_files(encrypted_folder, decrypted_folder, key)

    print("\nProcesso concluído!")


if __name__ == "__main__":
    main()

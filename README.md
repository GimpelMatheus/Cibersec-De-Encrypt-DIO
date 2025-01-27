# Cibersec-De-Encrypt-DIO

Este projeto é uma implementação prática de criptografia e descriptografia de arquivos, desenvolvido como parte de um estudo em cibersegurança para o curso da DIO (Digital Innovation One). Ele utiliza o algoritmo AES (Advanced Encryption Standard) para proteger arquivos de forma eficiente.

## Funcionalidades

- **Geração de Arquivos de Teste**: Cria 50 arquivos de teste com conteúdo aleatório na pasta `arquivos_teste`.
- **Criptografia**: Criptografa os arquivos de teste e salva os resultados na pasta `arquivos_criptografados`.
- **Descriptografia**: Descriptografa os arquivos criptografados e salva os resultados na pasta `arquivos_descriptografados`.

## Estrutura do Projeto

```plaintext
/
├── encrypt.py               # Classe para criptografar arquivos
├── decrypt.py               # Classe para descriptografar arquivos
├── main.py                  # Script principal para executar as funcionalidades
├── arquivos_teste/          # Pasta para os arquivos de teste gerados
├── arquivos_criptografados/ # Pasta para os arquivos criptografados
└── arquivos_descriptografados/ # Pasta para os arquivos descriptografados
```

## Pré-requisitos

Certifique-se de ter instalado:

- **Python 3.7+**
- Bibliotecas necessárias:
  - `pyaes`

Para instalar a biblioteca `pyaes`, use o seguinte comando:

```bash
pip install pyaes
```

## Como Executar

1. Clone este repositório para sua máquina local:

```bash
git clone https://github.com/GimpelMatheus/Cibersec-De-Encrypt-DIO.git
```

2. Navegue até o diretório do projeto:

```bash
cd Cibersec-De-Encrypt-DIO
```

3. Execute o script principal:

```bash
python3 main.py
```

4. O script realizará as seguintes etapas:
   - Gerar 50 arquivos de teste em `arquivos_teste/`.
   - Criptografar os arquivos e salvá-los em `arquivos_criptografados/`.
   - Descriptografar os arquivos criptografados e salvá-los em `arquivos_descriptografados/`.

## Exemplo de Saída

O script exibirá mensagens no console para indicar o progresso:

```plaintext
1. Gerando arquivos de teste...
50 arquivos de teste criados ou já existentes em 'arquivos_teste'.

2. Criptografando arquivos de teste...
Arquivo criptografado salvo em: arquivos_criptografados/teste_1.txt.ransomwaretroll
...

3. Descriptografando arquivos criptografados...
Arquivo descriptografado salvo em: arquivos_descriptografados/teste_1.txt
...

Processo concluído!
```

## Sobre o Projeto

Este projeto foi desenvolvido como parte de um estudo sobre cibersegurança, com foco em criptografia e proteção de dados. Ele demonstra conceitos básicos de como proteger arquivos contra acessos não autorizados usando o algoritmo AES.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests para melhorar este projeto.

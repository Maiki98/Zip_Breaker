import pyzipper
from datetime import datetime
import itertools
import os

#Aqui tu vai botar os parâmetros dos caracteres, normalmente deixo caracteres especiais também

def gerar_combinacoes(min_length, max_length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|:;"<>,.?/~`'
    combinations = []

    for length in range(min_length, max_length + 1):
        combinations.extend([''.join(seq) for seq in itertools.product(characters, repeat=length)])

    return combinations

#Lembrar de deixar o arquivo na mesma pasta do script

def tentar_descompactar_arquivo(arquivo_zip, min_length, max_length):
    combinations = gerar_combinacoes(min_length, max_length)
    print(f'\n{datetime.strftime(datetime.now(), "%H:%M:%S")} >> Gerando Combinacoes, Aguarde...')

    for combination in combinations:
        try:
            with pyzipper.AESZipFile(arquivo_zip, 'r') as zip_file:
                zip_file.extractall(pwd=combination.encode(), path='data')
            print(f'\n{datetime.strftime(datetime.now(), "%H:%M:%S")} >> Senha encontrada, pode estourar um champagne: {combination}')
            return combination
        except Exception as e:
            if "Bad password" in str(e):
                continue
            elif "No such file or directory" in str(e):
                print(f'\n{datetime.strftime(datetime.now(), "%H:%M:%S")} >> Arquivo ZIP não encontrado: {arquivo_zip}')
                break
            else:
                print(f'Erro: {e}')
                break

    print(f'\n{datetime.strftime(datetime.now(), "%H:%M:%S")} >> Senha não encontrada. FUDEU AMIGÃO')

if __name__ == "__main__":
    # Diretório atual do script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Define o nome do zip
    arquivo_zip = os.path.join(script_directory, "master.zip")

    # Intervalo de caracteres que tu acha que tem a senha, good luck
    min_length = 4
    max_length = 32

    senha_encontrada = tentar_descompactar_arquivo(arquivo_zip, min_length, max_length)
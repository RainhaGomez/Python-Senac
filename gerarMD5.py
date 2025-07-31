#Biblioteca para calcular funções de hash md5, sha-1, sha-256 e outros.
import hashlib
#
arquivo = input('Digite o nome do arquivo: ')

#Try tratamento de erro para evitar que o programa quebre caso o arquivo não exista. Bloco, Código e a Excessão.
try:
#With garante que o arquivo em modo binário será fechado corretamente após o uso.
    with open(arquivo,'rb') as f:
#Cria um objeto hash usando o algoritmo md5.
        md5 = hashlib.md5()
#Lê o arquivo em blocos de 4096 bytes para arquivos grandes, evitando o consumo excessivo de memória.
        for chunk in iter(lambda: f.read(4096), b""):
#adiciona o conteúdo do bloco ao hash.
            md5.update(chunk)
#Exibe o hash md5 em formato hexadecimal.
            print(f"MD5: {md5.hexdigest()}")
#fechamento do bloco try.
except FileExistsError:
    print('Arquivo não encontrado.')
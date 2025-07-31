'''
TRABALHANDO COM ARQUIVO TXT
r   Abre o arquivo somente para leitura. o arquivo já deve existir.
r+  Abre o arquivo para a leitura e escrita. O arquivo deve existir (Cria ou reescreve no arquivo existente a partir da primeira linha e apaga tudo para reescrever)
w   Abre o arquivo somente para escrita, no início do arquivo. Apagará o conteúdo do arquivo se ele já existir. Criará um novo arquivo se ele ainda não existir.
w+  Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
a   Acrescentar e cria o arquivo se não existir - Abre o arquivo para escrita no final. Não apaga o conteudo preexistente.
a+  Abre o arquivo para a escrita no final do arquivo de leitura. 
FUNÇÃO open(), após a declaração da variavél que receberá a função, necessita de sois parâmetros: o nome do arquivo e depois o modo como abrir esse arquivo.
Sintaxe: arquivo = open('arquivo.txt','w')

FUNÇÃO write(), é utilizada para gravar informações em um arquivo existente.
Sintaxe: arquivo.write('aula prática de Python')

FUNÇÃO close(), encerrar o arquivo após sua utilização. IMPORTANTE: Nunca abra 2x antes de fechar!!!

FUNÇÃO read(), leitura de _todo o conteúdo do arquivo
Sintaxe: leitura=open('arquivo.txt', 'r')
         print leitura.reade()
         leitura.close()
'''
'''
Criar arquivo
arquivo = open('arqTexto.txt','w')
arquivo.write('Curso de Python \n')
arquivo.write('Aula prática de programação.')
arquivo.close()

#Ler arquivo
leitura = open('arqTexto.txt', 'r')
print(leitura.read())
leitura.close()

arquivo = open('arqTexto.txt', 'a')
arquivo.write('Curso de Python com lógica de programação. \n')


valores = [100, 200, 300, 400, 500, 690, 800, 1000]
for valor in valores:
    arquivo.write(str(valor) + '\n')
    arquivo.close()

leitura = open('arqTexto.txt', 'r')    
print(leitura.read())
leitura.close()
'''
with open ('arqTexto.txt', 'r+') as arquivo:
    for valor in arquivo:
        print (valor)
    arquivo.write('1997' + '\n')
    print(valor)
arquivo.close()
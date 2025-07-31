arquivo = input('Informe o nome do Arquivo: ')
#Try = Localizar
try: 
  with open(arquivo, 'r') as f:
    linhas = f.readlines()
    print(f'O arquivo tem {len(linhas)} linhas.')
except FileExistsError:
    print('Arquivo não encontrado')
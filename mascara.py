'''
FORMATAÇÃO DE MÁSCARA
Assim como outras linguagens, é possível utilizar identificadores para representaros tipos de dados armazenados nas variáveis que devem ser exibidos na tela.
O Python utiliza a formatação comum entre várias linguagens de desenvolvimento para máscaas.

Exemplo na tabela abaixo de Máscara, Tipo de dados e Descrição:

%d  ou  %i      Int(inteiro)       Exibe o valor inteiro.
%f              Float ou double    Exibe um valor decimal.
%id             Long               Exibe um número inteiro longo
%e ou %E        Float e double     Exibe um número exponencial (numéro científico )
%c              Char (caractere)   Exibe um caractere
%o              Int                Exibe um número inteiro em formato octal
%x ou %X        Int                Exibe um número Inteiro no formato Hexadecimal.
%s              Char               Exibe uma cadeira DE CARACTERES (STRING)
%R              boolean            Exibe True ou False (Verdadeiro ou dalso).
Veja exemplos abaixo de aplicação:

'''
fruta = 'Laranja'
print(fruta)
print('Meu suco favorito é de' + fruta) #Usar, por padrão
print('Meu suco favorito é de', fruta)
print('Suco de %s é o meu favorito' %fruta)

#Exercício: exiba a mensagem "suco de Laranja é o meu favorito, amo Laranja."
print('Suco de %s é o meu favorito'%fruta, 'amo %s'  %fruta )
print('Suco de %s é o meu favorito, amo %s'%(fruta, fruta))
print('Suco de {0} é o meu favorito, amo {0}!!!' .format(fruta)) #O {} Representa o unica variavel, a primeira criada.

cor0 = 'Azul'
cor1 = 'Vermelha'
cor2 = 'Preta'
print('Gosto do céu {}, a flor {} e para o carro preferido a cor {}'.format(cor0, cor1, cor2))
print('Gosto do céu {0}, a flor {1} e para o carro preferido a cor {0}'.format(cor0, cor1, cor2))

conta= 10/3
print(conta)
print('O valor da conta é %f' %conta)
print('O valor da conta é %i' %conta)
print('O valor da conta é {}'.format(conta))#Sem o número nas {} ele já conta conta como a primeira variavél, nesse caso o 0
print('O valor da conta é %.2f' %conta)#casas decimais
print('O valor da conta é {:.2f}'.format(conta))#A direita 2

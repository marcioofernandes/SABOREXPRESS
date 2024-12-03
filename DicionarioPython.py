##Função print 
""" Estrutura
print (*Objetcs, sep= ' ', end = '\n', file=none, flush=False)
objetcs = é o conjunto de objetos cujo conteúdo será exibido 
sep = separador a ser usado, padrão é um branco
end= contém o caractere a ser enviado para a saido final, o padrão é pulo de linha 
file = define o arquivo de saida 
flush = se for True indica que o buffer de saída deve ser esvaziado. Seu valor padrão é False """

print ("Python na Escola de Programação da Alura")

##2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = "Marcio Fernandes"
idade = "35"

print (f"Meu nome é {nome} e tenho {idade} anos")

# Criação das Variáveis
nome2 = 'Lais'
idade2 = 24

# Abordagem mais simples
print('Meu nome é',nome2,'e tenho',idade2,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome2} e tenho {idade2} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome2,idade2))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome2,idade2))

##3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

print ("A\n")
print ("L\n")
print ("U\n")
print ("R\n")
print ("A\n")

##Para imprimir o valor de pi arredondado, temos algumas possíveis abordagens:

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

# Expressões Aritméticas 

a = 10
b = 20 

c = a + b # soma de a + b 
c = a - b # subtração 
c = a * b # multipiclação 
c = a / b # divisão 
c = a // b # divisão de numero inteiro 
c = a % b # calcula o resto da divisão de A por B 
c = -a # negativa o valor de A 
c = a ** b # eleva A por B 

#Atribuição incremental 
a = a + 1    # ou
a +=1 

# importar biblioteca
# from "biblioteca" import "função desejada"
#ou 
# import "Biblioteca" - trás a biblioteca inteira 

import math 
#quando importamos a biblioteca inteira, é necessário informar a biblioteca na frente da função, ou se usar o FROM, não tem essa necessidade 

x = math.sqrt (49)
print (x) 

# link para a biblioteca math: https://docs.python.org/3/library/math.html
# link para a biblioteca cmath: https://docs.python.org/3/library/cmath.html

# A função input ()

D = input ("Digite algo aqui para gravar: ") # neste caso, tudo que for digitado, mesmo número será apresentado como string
print (D)
type(D)
E = int(input(" Agora digite um numero: ")) 
F = float(input(" Agora digita um número real: "))




#Condicionais 

A= int (input("Digite a: "))
B = int (input("Digite B: "))

if B == 0:
    print ("Não é possivel calcular a divisão")

else:
    R = A / B 
    print (B)






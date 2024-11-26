##1 - Imprima a frase: Python na Escola de Programação da Alura.

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
print('Meu nome é %s e tenho %i anos.'%(nome,idade))


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

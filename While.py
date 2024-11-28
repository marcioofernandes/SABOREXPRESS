

x = 1
while x != 0: 
    x = int(input("Digite x: "))
    if x % 2 == 0: 
        print(f"{x} é par")
    else: 
        print(f"{x} é impar")
print ("Fim do Programa")



# lendo o código, enquanto x for diferente de 0, solicite o digito de um numero e calcula se é par ou impar, se for zero, acabe. 



while True:
   x = int(input("Digite x: "))
   if x == 0:
       break
   print (x)

print ("Fim do programa") 




# Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado.

n = int(input("Digite um numero: "))
cont = 1 

while cont <= 10:
    r =  cont * n 
    print (f"{cont} x {n} = {r}")
    cont = cont + 1 
print ('Fim do programa')


# Escreva um programa que mostre na tela os 10 primeiros termos de uma progressão aritmética (PA) com primeiro termo P e razão R. Os dois números P e R são inteiros e devem ser lidos do teclado.


p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão:  "))

cont = 1
while cont < 10:
    print(p)
    p = p + r
    cont = cont + 1
print ("Fim do programa") 



# Escreva um programa que leia do teclado um número inteiro D. Esse número deve ser obrigatoriamente maior que zero. Em seguida exiba na tela todos os números inteiros menores que 100 e que sejam divisíveis por D.

d = int (input ("Digite um numero inteiro: "))
if d < 0:
    print (" Numero inválido")
else:
    cont = 1 
    while cont < 100: 
        if cont % d == 0:
            print (cont)
        cont = cont + 1
print ("fim do programa")




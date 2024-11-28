""" 1   Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar. Lembrando
que para saber a paridade de um inteiro é preciso calcular o resto da sua divisão por 2. Se o resto for
0 o número é par, se o resto for 1 o número é ímpar."""

numero = int(input('Digite um numero qualquer: '))

if numero % 2 == 0: 
    print ('Este numero é par')
else: 
    print ('este numero é impar')

"""Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois. Se ambos
forem iguais, mostre qualquer um deles."""

numero2 = int(input("Digite um numero qualquer: "))
numero3 = int(input("Digite outro numero qualquer: "))

if numero2 < numero3: 
    print (f"{numero2} é o menor número entre os dois")

elif numero3 < numero2:
    print (f"{numero3} é o menor número entre os dois")

else:
    print (f"{numero2} e {numero3} são iguais")





    """Escreva um programa para exibir na tela o nome e a categoria de um lutador. O programa deve ler
um string para o nome e um número real para o peso. Conforme o peso ocorrerá o enquadramento
na categoria, segundo esta tabela (fictícia):"""

nome = input("Digite o nome do lutador: ")
peso = float(input("Digite o peso do lutador: "))

if peso < 52:
    categoria = 'Invalido'
elif peso < 65:
    categoria = "Leve"
elif peso < 79:
    categoria = "Ligeiro"
elif peso < 86:
    categoria = "Meio-médio"
elif peso < 90:
    categoria = "Médio"
elif peso < 100:
    categoria = "Meio-Pesado"
else: 
    categoria = "Pesado"

print (f"O lutador {nome} pesando {peso} está na categoria {categoria}")
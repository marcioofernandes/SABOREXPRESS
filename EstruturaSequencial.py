# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
d  = int(input("Digite um número: "))

""" print(f"O número informado foi {a}") """ 

# Faça um Programa que peça dois números e imprima a soma.

"""print (a+b)"""

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

media = (a+b+c+d) / 4

print (f"A média das notas {a, b, c, d} é {media}")

# Faça um Programa que converta metros para centímetros.

metro = float(input("Digite a quantidade de metros: "))

centimetros = metro * 100 
centimetros = int(centimetros)
print (f"{metro} metros é igual a {centimetros} centimetros")

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

pi = 3.1415926

raio = float(input("Digite o raio do circulo: "))
area = pi * (raio ** 2)
print (f"A área de um circulo de raio {raio} é {area:.2f}")

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float (input("Digite o lado do quadrado: "))
area2 = lado ** 2
dobro = area2 * 2
print (f"O dobro da area de um quadrado de lado {lado:.2f}m é {dobro:.2f}m2")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = float(input("Quanto você ganha por hora: "))
qtdHora = float(input("Quantas horas trabalhou no mês: "))
salario = valor * qtdHora 

print (f"Seu salario será R${salario:.2f} ")

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

graus_farenheit = float(input("Digite a temperatura em Farenheit: "))
graus_celsius = 5 * (graus_farenheit - 32) / 9

print (f"{graus_farenheit} graus Farenheit correspondem a {graus_celsius:.2f} graus Celsius")



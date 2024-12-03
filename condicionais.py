# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# uma condicional completa

PH = float(input("Digite um valor do PH: "))
if PH < 6.0:
    r = 'ácida'
elif PH < 7.0:
    r = " Levemente ácida"
elif PH == 7.0:
    r = "Neutra"
elif PH < 8.0:
    r = "Levemente alcalina"
else: 
    r = 'Alcalina'

print (f"Com PH = {PH} a solução é {r}")
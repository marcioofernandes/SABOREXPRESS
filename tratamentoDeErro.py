
try: 
    a = int(input("Digite um valor para A: "))
    b = int(input("Digite um valor para B: "))
    r = a / b 
    print (r)
except ValueError: 
    print ("Digite apenas numeros inteiros")
except ZeroDivisionError: 
    print ("B não pode ser zero")
except: 
    print ("Não foi possível calcular a divisão")


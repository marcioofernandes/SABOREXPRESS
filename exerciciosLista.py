p = int (input ('Digite o primeiro termino: '))
r = int (input ('Digite a razão: '))
q = int (input ("Digite a quantidae de termos: "))

termos = [] 

a = 0 

while a < q: 
    termos.append (p)
    p = p + r 
    a = a + 1 
print ('\nLista resultante')
print (termos)
print ("fim do programa ")
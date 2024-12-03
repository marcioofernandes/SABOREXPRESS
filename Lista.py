L = [36, 24, 58, 64, 98, 10]

print("Exibição da lista completa:")
print(L)

print("\nExibição dos elementos individuais:")
i = 0
while i < len(L):  # Corrigida a condição do loop
    print(L[i], end="  ")  # Exibe elementos na mesma linha
    i += 1  # Incrementa o índice
print("\nFim da lista")  # Ajustado o texto e escape

# Adiciona elementos a lista

L.append (69)
L.append (77)
print (L)

# Substitui elementos da lista 

L [6] = 99 
print (L) 

# Deleta elementos da lista 

del L [3]
print (L)

# fatiamento

origem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
destino1 = origem [3:6] # começa na posição 3 e vai até a posição 5
print (f'destino1 {destino1}')
destino2 = origem [1:10:2] # começa do 1 e vai até 10 pulando de 2 em 2 
print (f"destino2 {destino2}")
destino3 = origem [:4] # não define o inicio e para na posição 4 
print (f"destino3 {destino3}")
destino4 = origem [2:] # não define o fim e começa na posição 2 
print (f"destino4 {destino4}")

#backup de lista 
bkuporigem = origem [:]
print (bkuporigem)


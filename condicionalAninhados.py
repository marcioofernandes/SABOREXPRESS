risco = input ('Digite baixo ou alto para o grau de risco: ')


if risco != "baixo" and risco != "alto":
    print (f"{risco} inválido.\n Digite 'baixo' ou 'alto'")
else:
    valor = float (input ("Digite o valor: ")) 
    if risco == "baixo":
        if valor < 1000.0:
            tipo = 'Poupança'
        else: 
            tipo = 'Renda Fixa' 

    else:
        if valor < 1000.0:
            tipo = "Bitcoins"
        else: 
            tipo = "Ações"

    print (f"Você deve investir em {tipo}")


numero= int(input("Digite um numero para saber seu fatorial"))
fat=1
multi=1
if numero<0:
    print("Inválido")
else:
    for fat in range(1,numero):
        if fat*(fat-1)!=0:
         multi=fat*multi
    print(f"O fatorial de {numero} é: {numero*multi}")

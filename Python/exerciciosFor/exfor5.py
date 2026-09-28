base= int(input("Digite um valor para a base"))
expoente= int(input("Digite um valor para o expoente"))
indicador=False
multi=base
valor=1
if expoente==0:
   print(f"{base} elevado a {expoente} = 1")
for valor in range (1,expoente+1):
    if valor<expoente:
        multi=multi*base
    else:
     print(f"{base} elevado a {expoente} = {multi}")
    


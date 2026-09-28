lista=[]
i=0
while i<5:
    num=int(input("Digite um número para a lista "))
    lista.append(num)
    i+=1
i=0
while i<len(lista):
    if lista[i]<0:
        lista[i]=0
    i+=1
print(f"A lista final trocando números negativos por 0 é: {lista}")

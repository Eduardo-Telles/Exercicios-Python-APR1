lista1=[]
lista2=[]
i=0
while i<3:
    num=int(input("Digite um número para a lista1"))
    lista1.append(num)
    i+=1
i=0
while i<3:
    num=int(input("Digite um número para a lista2"))
    lista2.append(num)
    i+=1
i=0
novalista=[]
while i<len(lista1):
    j=0
    while j<len(lista2):
        if lista1[i]==lista2[j]:
            novalista.append(lista1[i])
        j+=1
    i+=1
print(f"Os números que estão nas duas listas são: {novalista}")
    
     
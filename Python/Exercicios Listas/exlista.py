L=[]
qnt= int(input("Digite a quantidade de elementos para a lista"))
i=0
#Criando a lista adicionando elementos
while i<qnt:
    n= int(input("Digite números para a lista"))
    L.append(n)
    i+=1
print(L)
#Ímpares da lista
for i in range(len(L)):
    if L[i] % 2 !=0:
        print(L[i], end=" ")
print(" ")
print("*************")
#Pares da lista
for i in range(len(L)):
    if L[i] % 2 ==0:
        print(L[i], end=" ")
print(" ")
#Maior valor da lista
maior=L[0]
i=1
while i < len(L):
    if L[i] > maior:
        maior = L[i]
    i+=1
print(f"O maior valor é {maior}")
#Menor valor da lista 
menor= L[0]
i=1
for i in range(len(L)):
    if L[i] < menor:
        menor = L[i]
print(f"O menor numero é {menor}")
#somar toda a lista
somar=L[0]
i=1
while i < len(L):
    somar+=L[i]
    i+=1
print(f"a soma é {somar}")

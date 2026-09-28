lista=[]
listainv=[]
i=0
while i<5:
    num=int(input("Digite um número para a lista"))
    lista.append(num)
    i+=1
i=1
while i<=len(lista):
    listainv.append(lista[-i])
    i+=1
print(f" A lista inversa é: {listainv}")
    
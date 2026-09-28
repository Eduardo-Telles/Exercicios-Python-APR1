n= int(input("Digite a qnt de números que a lista terá"))
lista=[]
for i in range(n):
    num=int(input("Digite um número para a lista"))
    lista.append(num)

semrepeticao=[]
repetidos=[]
for num in lista:
    if num not in semrepeticao:
        semrepeticao.append(num)
    else:
        if num not in repetidos:
            repetidos.append(num)
print(lista)
print(semrepeticao)
print(repetidos)


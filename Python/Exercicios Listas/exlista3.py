lista=[]
sequencia=False
soma=0
multi=1
qnt=int(input("Digite a qntd de termos que a lista terá"))
i=0
while i<qnt:
    num=int(input("Digite números para a lista"))
    lista.append(num)
    if num%2==0:
        soma=soma+num
    else:
        multi=multi*num
    i+=1
print(lista)
print(f"A soma dos elementos pares é: {soma}")
print(f"A multiplicação dos numeros impares é: {multi}")
        
        
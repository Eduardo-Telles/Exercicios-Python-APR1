qnt= int(input("Digite a qnt de números que as listas terão"))
L1=[]
L2=[]
for i in range(qnt):
    num1=int(input("Digite um número para a lista1"))
    L1.append(num1)
for i in range(qnt):
    num2=int(input("Digite um número para a lista2"))
    L2.append(num2)
LF=[]
for i in range(qnt):
    Soma=L1[i]+L2[i]
    LF.append(Soma)
print(L1)
print(L2)
print(LF)

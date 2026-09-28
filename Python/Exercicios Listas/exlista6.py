qnt= int(input("Digite a qnt de números que as listas terão"))
L1=[]
LF=[]
for i in range(qnt):
    num=int(input("Digite um número para a lista"))
    L1.append(num)
for i in range(qnt):
    cubo=L1[i]**3
    LF.append(cubo)
print(LF)
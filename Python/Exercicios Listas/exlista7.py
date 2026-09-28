qnt=int(input("Digite a qnt de termos da lista"))
L1=[]
Linvertida=[]
for i in range(qnt):
    num=int(input("Digite um numero para a lista"))
    L1.append(num)
i=qnt-1
while i>=0:
    Linvertida.append(L1[i])
    i-=1
print(L1)
print(Linvertida)
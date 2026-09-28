qnt=int(input("Digite a qnt de termos da lista"))
L1=[]
for i in range(qnt):
    num=int(input("Digite um numero para a lista"))
    L1.append(num)
print(L1)
for i in range(qnt):
    if L1[i]%2==0:
        L1[i]=+1
    else:
        L1[i]=-1
print(L1)
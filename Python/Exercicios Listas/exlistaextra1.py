L1=[]
L2=[]
i=0
soma=0
while i<3:
    num=int(input("Digite um numero para a lista1"))
    L1.append(num)
    i+=1
i=0
while i<3:
    num2=int(input("Digite um numero para a lista2"))
    L2.append(num2)
    i+=1
i=0
while i<3:
    multi=L1[i]*L2[i]
    soma=soma+multi
    i+=1
i=0
while i<len(L1):
    print(f"[{L1[i]}]", end=" ")
    i+=1
print(" ")
i=0
while i<len(L2):
    print(f"[{L2[i]}]", end=" ")
    i+=1
print(" ")
print(f"o produto escalar é: {soma}")
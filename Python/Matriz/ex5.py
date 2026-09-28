matrizA=[]
matrizB=[]
n=int(input("informe o numero de linhas da matriz"))
m=int(input("informe o numero de colunas da matriz"))
lin=0
while lin < n:
    linha=[]
    print(f"Digite os valores da linha {lin} da matriz")
    col=0
    while col<m:
        num=int(input(f"entre com o valor da coluna {col}: "))
        linha.append(num)
        col+=1
    matrizA.append(linha)
    lin+=1
i=0
while i < len(matrizA):
    j=0
    while j < len(matrizA[i]):
        print(matrizA[i][j], end=" ")
        j+=1
    print()
    i+=1
p=int(input("Digite a proporção da matriz"))
q=int(input("Digite a proporção da matriz"))
lin=0
while lin < p:
    linha=[]
    print(f"Digite os valores da linha {lin} da matriz")
    col=0
    while col < q:
        num2=int(input(f"Entre com o valor da coluna {col}: "))
        linha.append(num2)
        col+=1
    matrizB.append(linha)
    lin+=1
i=0
while i < len(matrizB):
    j=0
    while j < len(matrizB[i]):
        print(matrizB[i[j]], end=" ")
        j+=1
    print()
    i+=1







matriz=[]
qlinha=2
qcoluna=3
i=0
while i < qlinha:
    linha=[]
    j=0
    while j< qcoluna:
        num=int(input(f"Digite um número para a linha {i+1} coluna {j+1}: "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    i+=1
print(matriz)
transposta=[]
j=0
i=0
while j < qcoluna:
    linha=[]
    i=0
    while i < qlinha:
        linha.append(matriz[i][j])
        i+=1
    transposta.append(linha)
    j+=1
print(transposta)
i=0
j=0
while i<len(matriz):
    j=0
    while j< len(matriz[i]):
        print(matriz[i][j], end=" " )
        j+=1
    print()
    i+=1 
i=0
j=0
while i<len(transposta):
    j=0
    while j< len(transposta[i]):
        print(transposta[i][j], end=" " )
        j+=1
    print()
    i+=1 


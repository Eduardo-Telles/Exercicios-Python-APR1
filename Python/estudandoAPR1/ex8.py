matriz=[]
qlinha=3
qcoluna=3
i=0
while i<qlinha:
    j=0
    linha=[]
    while j<qcoluna:
        num=int(input(f"Digite um número para a linha {i+1} coluna {j+1} "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    i+=1
print("A matriz é: ")
i=0
while i<len(matriz):
    j=0
    while j<len(matriz[i]):
        print(matriz[i][j], end=" ")
        j+=1
    print()
    i+=1
print("A soma da diagonal da matriz é:")
i=0
soma=0
while i < len(matriz):
    j=0
    while j < len(matriz[i]):
        if i==j:
            soma=soma+matriz[i][j]
        j+=1
    i+=1
print(soma)
        

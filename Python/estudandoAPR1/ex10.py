qlinha=4
qcoluna=4
matriz=[]
i=0
j=0
while i < qlinha:
    j=0
    linha=[]
    while j < qcoluna:
        num=int(input(f"Digite um numero para a linha {i+1} e coluna {j+1} "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    i+=1
print(matriz)
i=0
j=0
while i<len(matriz):
    j=0
    while j < len(matriz[i]):
        print(matriz[i][j], end=" ")
        j+=1
    print()
    i+=1
achar=int(input("Procure um número na matriz "))
i=0
j=0
achou=False
while achou==False:
    while i < len(matriz):
        j=0
        while j < len(matriz[i]) and achou==False:
            if achar==matriz[i][j]:
                print(f"achou, o número está na linha {i+1} na coluna {j+1}")
                achou=True
            else:
                if i==(len(matriz))-1 and j==(len(matriz[i])-1):
                    print("Não existe esse número na matriz")
                    achou=True
            j+=1
        i+=1

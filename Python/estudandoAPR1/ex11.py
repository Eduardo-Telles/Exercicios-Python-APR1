matriz=[]
qlinha=3
qcoluna=3
i=0
while i < qlinha:
    j=0
    linha=[]
    while j < qcoluna:
        num=int(input("Digite um número "))
        linha.append(num)
        j+=1
    i+=1
    matriz.append(linha)
i=0
j=0
print("A matriz criada foi:")
while i < len(matriz):
    j=0
    while j < len(matriz[i]):
        print(matriz[i][j], end=" ")
        j+=1
    print()
    i+=1
i=0
j=0
transposta=[]
while j < qcoluna:
    i=0
    linha=[]
    while i < qlinha:
        linha.append(matriz[i][j])
        i+=1
    j+=1
    transposta.append(linha)
print(transposta)
i=0
j=0
while i < len(transposta):
    j=0
    while j < len(transposta[i]):
        print(transposta[i][j], end=" ")
        j+=1
    print()
    i+=1
i=0
j=0
achou=False
while i < len(matriz) and achou==False:
    j=0
    while j < len(matriz[i]) and achou ==False:
        if matriz[i][j]!=transposta[i][j]:
            print("Não simétrica")
            achou=True
        else:
            if i==(len(matriz)-1):
                print("Matriz simétrica")
                achou=True
        j+=1
    i+=1

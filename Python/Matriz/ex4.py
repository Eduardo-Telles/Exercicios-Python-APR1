matriz=[]
#populando a matriz a partir de dados fornecidos pelo usuário
N=int(input("Informe o numero de linhas da matriz"))
M=int(input("Informe o numero de colunas da matriz"))
lin=0
while lin < N:
    linha=[]#guarda os valores da linha lin
    print(f"Digite os valores da linha {lin} da matriz: ")
    col=0
    while col < M:#constrói cada linha da matriz
        num=int(input(f"Entre com o valor da coluna {col}: "))
        #inclui valor na lista linha
        linha.append(num)
        col+=1
    #inseri cada linha na matriz
    matriz.append(linha)
    lin+=1
i=0
#percorre cada linha i da matriz
while i < len(matriz):
    j=0
    #percorre cada coluna j da linha i
    while j < len(matriz[i]):
        print(matriz[i][j], end=" ")
        j+=1
    print()
    i+=1
i=0
qntd=0
while i < len(matriz):
    j=0
    somadalinha=0
    while j < len(matriz[i]):
        somadalinha+=matriz[i][j]
        j+=1
        if somadalinha==0 and j==len(matriz[i]):
            print("linha nula")
            qntd+=1
    i+=1
print(f"Qntd de linhas nulas: {qntd}")
qnt=0
i=0
while i < len(matriz):
    j=0
    somadacoluna=0
    while j < len(matriz[i]):
        somadacoluna+=matriz[j][i]
        j+=1
        if somadacoluna==0 and j==len(matriz[i]):
            print("Coluna nula")
            qnt+=1
    i+=1
print(f"A qntd de colunas nulas: {qnt}")


        
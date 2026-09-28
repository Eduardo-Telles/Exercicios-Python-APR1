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
#lendo maior
i=0
maior=0
resultmaior=matriz[0][0]
while i<len(matriz):
    j=0
    while j < len(matriz[i]):
        if matriz[i][j]>resultmaior:
            resultmaior=matriz[i][j]
        j+=1
    i+=1
#lendo menor
i=0
menor=0
resultmenor=matriz[0][0]
while i<len(matriz):
    j=0
    while j < len(matriz[i]):
        if matriz[i][j]<resultmenor:
            resultmenor=menor
        j+=1
    i+=1
print(f"O maior número da matriz é: {resultmaior}")
print(f"O menor número da matriz é: {resultmenor}")


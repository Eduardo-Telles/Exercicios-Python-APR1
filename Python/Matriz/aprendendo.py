matriz=[]
#populando a matriz a partir de dados fornecidos pelo usuário
linhas=int(input("Informe o numero de linhas da matriz"))
colunas=int(input("Informe o numero de colunas da matriz"))
lin=0
while lin < linhas:
    linha=[]#guarda os valores da linha lin
    print(f"Digite os valores da linha {lin} da matriz: ")
    col=0
    while col < colunas:#constrói cada linha da matriz
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



matriz=[]
#populando a matriz a partir de dados fornecidos pelo usuário
N=int(input("Digite a dimensão da matriz"))
lin=0
while lin < N:
    linha=[]#guarda os valores da linha lin
    print(f"Digite os valores da linha {lin} da matriz: ")
    col=0
    while col < N:#constrói cada linha da matriz
        num=int(input(f"Entre com o valor da coluna {col}: "))
        #inclui valor na lista linha
        linha.append(num)
        col+=1
    #inseri cada linha na matriz
    matriz.append(linha)
    lin+=1
i=0
print("Matriz")
#percorre cada linha i da matriz
while i < len(matriz):
    j=0
    #percorre cada coluna j da linha i
    while j < len(matriz[i]):
        print(matriz[i][j], end=" ")
        j+=1
    print()
    i+=1
#calculando a matriz transposta da ja
transposta=[]
j=0
i=0
while j < N:
    linha=[]#representa cada linha da matriz transposta
    i=0
    while i < N:
        linha.append(matriz[i][j])
        i+=1
    transposta.append(linha)
    j+=1

print("Matriz Tranposta:")
#imprimindo a matriz transposta
i=0
j=0
while i<len(transposta):
    j=0
    while j<len(transposta[i]):
        print(transposta[i][j], end=" ")
        j+=1
    print()
    i+=1
if matriz==transposta:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")
   
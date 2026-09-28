matriz=[]
n=3
i=0
while i < n:
    j=0
    linha=[]
    while j < n:
        num=int(input(f"Digite um número para a linha {i+1} coluna{j+1} "))
        linha.append(num)
        j+=1
    i+=1
    matriz.append(linha)
i=0
while i < len(matriz):
    j=0
    while j < len(matriz[i]):
        print(matriz[i][j], end=" ")
        j+=1
    print()
    i+=1
i=0
cont=True
verdadeiro=False
while i < len(matriz) and cont==True:
    j=0
    soma=0
    while j < len(matriz[i]) and cont==True:
        soma+=matriz[i][j]
        if i==0 and j==2:
            final=soma
        if i==1 and j==2:
            if final!=soma:
                print("Não quadrada")
                cont=False
        if i==2 and j==2:
            if final!=soma:
                print("Não quadrada")
                cont=False
            else:
                verdadeiro=True
                cont=False
        j+=1
    i+=1
i=0
soma=0
while verdadeiro==True and i<len(matriz):
    j=0
    soma=0
    while j < len(matriz[i]) and verdadeiro==True:
        soma+=matriz[j][i]
        if j==0 and i==2:
            if final!=soma:
                verdadeiro=False
                print("Não é quadrado perf")
        if j==1 and i==2:
            if final!=soma:
                verdadeiro=False
                print("Não é quadrado perf")
        if j==2 and i==2:
            if final!=soma:
                verdadeiro=False
                print("Não é quadrado perf")
            else:
                verdadeiro=False
                print("quadrado perf")
        j+=1
    i+=1




        
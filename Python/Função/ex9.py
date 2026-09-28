def criar_lista(lista,tamanho):
    print("digite número(s) para a lista")
    for i in range (tamanho):
        num=int(input())
        lista.append(num)

def diferenca(listaA,listaB,listaC):
    for i in range(len(listaA)):
        achou=False
        for j in range(len(listaB)):
            if listaA[i]==listaB[j]:
                achou=True 
        if achou==False:
            listaC.append(listaA[i])
    for i in range(len(listaB)):
        achou=False
        for j in range(len(listaA)):
            if listaB[i]==listaA[j]:
                achou=True
        if achou==False:
            for x in range(len(listaC)):
                if listaB[i]==listaC[x]:
                    achou=True
            if achou==False:
                listaC.append(listaB[i])

        

def imprimir(lista):
    print("Lista:")
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()
    

def main():
    A=[]
    B=[]
    C=[]
    tamanho=int(input("Informe o tamanho da lista"))
    criar_lista(A,tamanho)
    criar_lista(B,tamanho)
    diferenca(A,B,C)
    imprimir(C)
main()
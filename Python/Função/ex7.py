#criar lista
def criar_lista(lista,tamanho):
    print("infome os números para a lista")
    for i in range(tamanho):
        num=int(input())
        lista.append(num)

def imprimir(lista):
    print("Lista:")
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

def intersecao(listaA,listaB,listaC):
    for i in range(len(listaA)):
        
        for j in range(len(listaB)):
            if (listaB[j])==(listaA[i]):
                listaC.append(listaB[j])
    return listaC

def main():
    A=[]
    B=[]
    C=[]        
    n=int(input("Informe o tamanho para a lista"))
    criar_lista(A,n)
    criar_lista(B,n)
    imprimir(A)
    imprimir(B)
    C=intersecao(A,B,C)
    imprimir(C)
main()
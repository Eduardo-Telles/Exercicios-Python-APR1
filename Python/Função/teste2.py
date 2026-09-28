def criar_lista(lista,tamanho):
    print("Digite os valores da lista: ")
    for i in range (tamanho):
        num= int(input())
        lista.append(num)

def imprimir_lista(lista):
    print(f"Imprimindo a Lista")
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

def calcular_uniao(listaA,listaB,listaC):
    for i in range(len(listaA)):
        listaC.append(listaA[i])
    for i in range(len(listaB)):
        achou=False
        j=0
        while j < len(listaC) and not achou:
            if listaB[i] == listaC[j]:
                achou=True
            j+=1
        if not achou:
            listaC.append(listaB[i])



def main():
    A=[]
    B=[]
    C=[]
    n=int(input("Informe a quantidade de elementos da lista"))
    #chama a função que cria a lista A
    criar_lista(A,n)
    #chama a função que cria a lista B
    criar_lista(B,n)
    #imprimindo as listas
    imprimir_lista(A)
    imprimir_lista(B)
    #Juntando as listas
    calcular_uniao(A,B,C)
    imprimir_lista(C)

main()
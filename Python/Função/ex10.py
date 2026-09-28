def criar_lista(lista,tamanho):
    print("Digite números para a lista")
    for i in range(tamanho):
        num=int(input())
        lista.append(num)

def uniao(A,B,C):
     for i in range(len(A)):
        C.append(A[i])
     for i in range(len(B)):
        achou=False
        j=0
        while j < len(C) and not achou:
            if B[i] == C[j]:
                achou=True
            j+=1
        if not achou:
            C.append(B[i])
def intersecao(A,B,I):
     for i in range(len(A)):
        
        for j in range(len(B)):
            if (B[j])==(A[i]):
                I.append(B[j])

def diferenca(A,B,D):
    for i in range(len(A)):
        if A[i] not in B:
            D.append(A[i])
    for x in range(len(B)):
        if B[x] not in A:
            D.append(B[x])
    
def main():
    A=[]
    B=[]
    C=[]
    I=[]
    D=[]
    tamanho=int(input("Digite quantos elementos a lista terá"))
    criar_lista(A,tamanho)
    criar_lista(B,tamanho)
    uniao(A,B,C)
    print(f"U={C}")
    intersecao(A,B,I)
    print(f"I={I}")
    diferenca(A,B,D)
    print(f"D={D}")
main()
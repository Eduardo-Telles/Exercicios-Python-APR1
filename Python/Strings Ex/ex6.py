def entrada():
    nome=input("Digite seu nome: ")
    return nome
def imprimir(nome):
    qntd=1
    for i in range(len(nome)):
        if i==0:
            pL=nome[i]
            print(pL)
        else:
            print(pL+nome[i])
            pL=pL+nome[i]
def main():
    nome=entrada()
    imprimir(nome)

main()
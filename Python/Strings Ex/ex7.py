def entrada():
    nome=input("Digite seu nome: ")
    return nome
def imprimircontrario(palavra):
    nome=""
    for i in range(1,len(palavra)):
        nome=nome+palavra[-i]
    nome+=palavra[0]
    return nome
def imprimir(palavra):
    print(palavra)
def main():
    nome=entrada()
    nomecontrario=imprimircontrario(nome)
    imprimir(nomecontrario)
main()
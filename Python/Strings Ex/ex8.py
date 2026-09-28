def entradas():
    palavras=input()
    return palavras
def contandoVogaiseEspaços(palavra):
    qntdvogal=0
    qntdespaços=0
    for i in range(len(palavra)):
        if palavra[i]=="a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U":
            qntdvogal+=1
        if palavra[i]==" ":
            qntdespaços+=1
    return qntdvogal,qntdespaços
def imprimir(algo):
    print(algo)
def main():
    print("Digite uma frase:")
    frase=entradas()
    qntdVogaiseEspaços=contandoVogaiseEspaços(frase)
    imprimir(qntdVogaiseEspaços)
main()
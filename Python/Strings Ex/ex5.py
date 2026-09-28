def entrada():
    frase=input("Digite uma frase: ")
    return frase
def analise(frase):
    palavras=1
    sempalavras=0
    if  frase=="":
        return sempalavras
    for i in range(len(frase)):
        if frase[i]==" ":
            palavras+=1
    return palavras
def imprimir(qntd):
    print(f"A qntd de palavras é  {qntd}")
def main():
    frase=entrada()
    qntdpalavras=analise(frase)
    imprimir(qntdpalavras)
main()
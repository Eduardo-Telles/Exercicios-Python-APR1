def entrada():
    palavra=input("Digite uma palavra: ")
    return palavra

def reconhechendopalindromo(palavra):
    cont=True
    for i in range(1,len(palavra)):
        if palavra[i-1]!=palavra[-i]:
            cont=False
    if cont==True:
        print(f"{palavra} É palíndromo")
    else:
        print(f"{palavra} Não é palíndromo")
def main():
    palavra=entrada()
    reconhechendopalindromo(palavra)
main()
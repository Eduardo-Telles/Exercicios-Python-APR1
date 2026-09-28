def entrada():
    palavra=input("Digite uma palavra: ")
    return palavra
def contrario(palavra,k):
    if k==len(palavra)-1:
        print(palavra[k])
        return palavra[k]
    else:
        print(palavra[k])
        return contrario(palavra,k+1)
def main():
    palavra=entrada()
    k=0
    resultado=contrario(palavra,k)
main()
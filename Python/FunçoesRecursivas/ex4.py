def entrada():
    palavra=input("Digite uma palavra: ")
    return palavra
def contrario(palavra,k):
    if k==0:
        print(palavra[0])
        return palavra[0]
    else:
        print(palavra[k])
        return contrario(palavra,k-1)
def main():
    palavra=entrada()
    k=len(palavra)-1
    resultado=contrario(palavra,k)
main()
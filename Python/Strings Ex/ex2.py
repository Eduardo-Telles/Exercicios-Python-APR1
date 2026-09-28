def entrada1():
    palavra=input("Digite uma palavra ")
    return palavra
def entrada2():
    letra=input("Digite a letra a ser removida ")
    return letra
def tirar1(palavra,letra):
    ret=""
    for i in range(len(palavra)):
        if palavra[i] != letra:
            ret=ret+palavra[i]
    return ret
def main():
    palavra=entrada1()
    letra=entrada2()
    tirar1(palavra,letra)
    print(tirar1(palavra,letra))
main()
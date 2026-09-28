def entrada1():
    palavra=input()
    return palavra
def tirar(p,l):
    achou=False
    nova_palavra = ""
    for i in range(len(p)):
        if p[i] == l and achou ==False:
            achou = True
        else:
            nova_palavra=nova_palavra+p[i]
    return nova_palavra
            
def main():
    print("Digite uma plavra")
    palavra=entrada1()
    print("Digite uma letra")
    letra=entrada1()
    nova=tirar(palavra,letra)
    print(nova)
main()
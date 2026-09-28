def entrada1():
    palavra=input("Digite a primeira palavra: ")
    return palavra
def entrada2():
    palavra=input("Digite a segunda palavra: ")
    return palavra
def igual(p1,p2):
    if p1==p2:
        print(f"{p1} e {p2} São iguais")
    else:
        print(f"{p1} e {p2} São diferentes")
def caracteres(p1,p2):
    l=[]
    cont=0
    for i in range(len(p1)):
        if p1[i] not in l:
            l.append(p1[i])
            cont=cont+1
    print(f"A qntd de caracteres sem repetir na primeira palavra é: {cont}")
    cont=0
    l=[]
    for i in range(len(p2)):
        if p2[i] not in l:
            l.append(p2[i])
            cont+=1
    print(f"A qntd de caracteres sem repetir na segunda palavra é {cont}")
def main():
    palavra1=entrada1()
    palavra2=entrada2()
    igual(palavra1,palavra2)
    caracteres(palavra1,palavra2)
    
main()
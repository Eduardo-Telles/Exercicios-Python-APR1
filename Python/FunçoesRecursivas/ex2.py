def Pot(x,n):
    if n==0:
        return 1
    if n>0:
        return x * Pot(x,n-1) 
def entradas():
    num=int(input("Digite um número"))
    return num
def main():
    x=entradas()
    n=entradas()
    resultado=Pot(x,n)
    print(resultado)
main()
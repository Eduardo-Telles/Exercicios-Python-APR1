def entradas():
    num=int(input("Digite um número"))
    return num
def mdc(x,y):
    if x>=y and x%y==0:
        return y
    elif x<y:
        return mdc(y,x)
    else:
        return mdc(y,x%y)
def main():
    print("Digite dois números para descobrir o MDC deles")
    x=entradas()
    y=entradas()
    resultado=mdc(x,y)
    print(resultado)
main()
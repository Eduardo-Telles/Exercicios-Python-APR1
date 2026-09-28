def entradas():
    num=int(input("Digite um número: "))
    return num
def resto(x,y):
    if x%y==0:
        return 0
    elif x<y:
        return x
    else:
        return resto(x-y,y)

def main():
    print("Programa paracalcular resto de divisão! Informe dois números")
    x=entradas()
    y=entradas()
    result=resto(x,y)
    print(result)
main()
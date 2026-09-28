def entradas():
    num=int(input("Digite o número de termos"))
    return num
def fibo(x,y):
    if x==0:
        return 0
    else:
        return y+fibo(x-1,y+1)
def main():
    print("Digite o número de termos para descobrir a sequência de Fibonacci!")
    x=entradas()
    inicio=0
    result=fibo(x,inicio)
    print(result)
main()
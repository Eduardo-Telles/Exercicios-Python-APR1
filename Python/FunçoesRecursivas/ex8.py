def entradas():
    num=int(input("Digite um número!"))
    return num
def fat(x):
    if x==0:
        return 1
    else:
        return x * fat(x-1)
def main():
    x=entradas()
    result=fat(x)
    print(result)
main()
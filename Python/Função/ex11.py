def anagrama(a,b):
    achou=False
    if len(b)!=len(a):
        print("não é anagrama")
        achou=True
    if achou==False:
        for i in range(len(a)):
            if a[i] not in b:
                print("não é anagrama")
                achou=True
    if achou==False:
        for i in range(len(b)):
            if b[i] not in a:
                print("não é anagrama")
                achou=True
    if achou==False:
        print("É anagrama")
        achou=True

def main():
    print("Digite uma palavra")
    a=str(input())
    print("Digite outra palavra")
    b=str(input())
    anagrama(a,b)
main()
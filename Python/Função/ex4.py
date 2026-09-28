
def receber(num):
    if num>0:
        print(1)
    elif num<0:
        print(-1)
    else:
        print(0)

def main():
    print("Informe um número")
    num=int(input(""))
    receber(num)
main()


def InteiroPositivo(n):
    if type(n)==int and n>=0:
       return True
    else:
        return False
def main():
    L=[10,"teste",26,"outra coisa",5.6]
    i=0
    while i < len(L):
        if InteiroPositivo(L[i]) == True:
            print(f"{L[i]} é um inteiro")
        else:
            print(f"{L[i]} não é um inteiro")
        i+=1
main() 
def qntd():
    qnt=int(input("Digite quantos numeros terá o vetor"))
    return qnt
def vetor(q):
    v=[]
    for i in range(q):
        num=int(input("Digite um numero parao vetor"))
        v.append(num)
    return v
def s(k,v,n):
    if k==0:
        return v[0]
    if k>=1 and k<n:
        return v[k]+s(k-1,v,n)
def main():
    n=qntd()
    v=vetor(n)
    k=n-1
    resultado=s(k,v,n)
    print(f"A soma do vetor é {resultado}")
main()
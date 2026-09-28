n= int(input("Digite um número"))
r= int(input("Digite uma numero para a razão"))
x=1
soma=0
while x<=n :
    multi=r*x
    print(multi)
    soma=multi+soma
    x+=1
print(soma)

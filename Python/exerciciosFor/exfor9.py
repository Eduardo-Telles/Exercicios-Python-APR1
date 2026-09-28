numero= int(input("Digite um número"))
serie=0
termos=1
m=3
soma=0
total=0
for termos in range (0,numero+1):
    if termos>1:
        serie=(f"{termos}/{m}")
        div=termos/m
        m=m+2
        soma=div+soma
        print(f"{serie} = {div}")
print(f"Total={soma+1}")
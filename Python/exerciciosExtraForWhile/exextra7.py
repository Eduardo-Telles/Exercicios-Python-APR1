x=int(input("Digite um numero"))
y=int(input("Digite um numero"))
i=y+1
achou=False
while not achou:
    i-=1
    if y%i==0:
        if x%i==0:
            achou=True
print(f"O MDC de {x} e {y} é : {i}")

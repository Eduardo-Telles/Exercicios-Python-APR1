x=int(input("Digite um numero"))
y=int(input("Digite um numero"))
i=0
j=0
achou=False
while not achou:
    i+=1
    multi=x*i
    j=0
    while j<i:
        j+=1
        if multi==y*j:
            achou=True
print(f"O MMC é: {multi}")

    

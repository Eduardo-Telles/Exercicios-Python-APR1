base= int(input("Digite uma base"))
exp=int(input("Digite um expoente"))
i=1
result=1
achou=False
while achou==False:
    if exp==0:
        result=1
        achou=True
    else:
        while i<=exp:
            i+=1
            result=result*base
        achou=True
print(result)


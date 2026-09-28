num= int (input("Digite um número"))
achou=False
while achou==False:
    if num%2==0:
        if num>100:
            print("Número par e maior que 100")
            achou=True
        else: 
            print("Número par menor que 100")
            achou=True
    else:
        if num<100:
            print("Número impar menor que 100")
            achou=True
        else:
            achou=True
            print("Número impar maior que 100")
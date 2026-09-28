num = int(input("Digite um número maior que 1 para saber se ele é primo"))
div = 2
if num<=1:
    print("Esse número não pode ser consultado")
while num%div!=0:
    div=div+1
if num == div:
    print("O número é primo")
else:
    print("O número não é primo")
    
  

numero= int(input("Digite um numero maior que 1 para saber se é primo"))
divisor= 2
naoprimo= False
if numero>=divisor:
 for divisor in range (2,numero+1) :
  if divisor==numero and naoprimo==False: 
    print(f"O número {numero} é primo")
  elif numero%divisor==0 and naoprimo==False:
   print(f"O numero {numero} não é primo")
   naoprimo=True
    
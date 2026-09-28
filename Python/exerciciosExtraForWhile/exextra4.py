import random
numero=random.randint(0,101)

for x in range(0,101):
 tentativa=int(input("Acerte o número"))
 if tentativa<numero:
  print("tente um número maior")
 elif tentativa>numero:
   print("tente um número menor")
 elif numero==tentativa:
    print(f"Você acertou o número é {tentativa}")
    print({numero})
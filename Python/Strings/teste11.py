import string
nro_ok=False
while not nro_ok:
 nro=input("Digite um número inteiro positivo: ")
 nro_ok=True
 for i in range(len(nro)):
    if nro[i] not in string.digits:
        nro_ok=False
 if not nro_ok:
    print("O valor digitado não é um número inteiro positivo!")
nro=int(nro) #faz a conversão
print("O valor digitado é: ",nro)
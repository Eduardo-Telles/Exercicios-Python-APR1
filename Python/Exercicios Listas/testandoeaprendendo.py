numeros = []

numero = int(input("Digite um numero (-1 para parar): "))

while numero != -1:
    numeros.append(numero)
    numero = int(input("Digite um numero (-1 para parar): "))
print(f"Sequencia original: {numeros}")
cubos = []
i = 0

while i < len(numeros):
    cubos.append(numeros[i] ** 3)
    i += 1

print(f"Sequencia ao cubo:")
i = 0
while i < len(cubos):
    print(cubos[i], end=" ")
    i += 1

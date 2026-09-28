palavra=input("Digite uma palavra: ")
caractere=input("Digite um caractere a ser contado: ")
contador = 0
for i in range(len(palavra)):
 if palavra[i] == caractere:
    contador = contador + 1
print(f"A letra {caractere} aparece {contador} vezes na palavra {palavra}")
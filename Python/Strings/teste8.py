palavra=input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
str_sem_vogais = ""
for i in range(len(palavra)):
 if palavra[i] not in vogais:
    str_sem_vogais = str_sem_vogais + palavra[i]
print(str_sem_vogais)
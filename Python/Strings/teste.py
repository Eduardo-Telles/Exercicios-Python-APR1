frase= "Eu gosto de chocolate"
sorteio=[5,4,-3,5,11]
acertos=0
for i in sorteio:
    resposta= input(f"Qual o caractere de índice {i} ")
    if frase[i]==resposta:
        print("Parabéns vc acertou!")
        acertos+=1
    else:
        print(f"Vc errou. O caractere de indice {i} é: {frase[i]}")
print(f"Você acertou {acertos} de {len(sorteio)} perguntas.")

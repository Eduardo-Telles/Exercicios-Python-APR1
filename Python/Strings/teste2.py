ini, fim = 3, 7
texto = "Eu posso ajudar respondendo perguntas no fórum!"
fatia = texto[ ini : fim ]
print("Seja o texto: ", texto)
resposta = input(f"Digite a string que corresponde à fatia texto[{ini}:{fim}] = ")
if resposta == fatia:
 print("Muito bem, você acertou!!")
else:
 print("Você escreveu : ", resposta)
 print("mas o valor correto é: ", fatia)
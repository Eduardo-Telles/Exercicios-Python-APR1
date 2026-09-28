ini, fim, passo = 3, 13, 2
texto = "Eu posso ajudar respondendo perguntas no fórum!"

fatia = texto[ ini : fim : passo ]
resposta = input(f"Digite a string que corresponde à fatia texto[{ini}:{fim}:{passo}] = ")
if resposta == fatia:
 print("Muito bem, você acertou!!")
else:
 print("Você escreveu : ", resposta)
 print("mas o valor correto é: ", fatia)
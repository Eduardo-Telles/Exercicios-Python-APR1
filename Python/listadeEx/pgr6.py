''' Uma determinada loja está fazendo promoções de vendas. Qualquer 
compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se 
a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto 
será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de 
20%.
Faça um programa que leia o quanto o cliente gastou e escreva o valor da 
conta já com os descontos.'''
compra = float(input("Digite o valor da compra"))
desconto20 = (compra - compra*0.2)
desconto10 = (compra - compra*0.1)
desconto5 = (compra - compra*0.05)
if compra >= 200.00:
    print(f"O valor sem desconto foi {compra}")
    print(f"A compra com desconto ficou: {desconto20}")
elif compra > 100.00:
    print(f"O valor sem desconto foi: {compra}")
    print(f"A compra com desconto ficou: {desconto10}")
else: 
    print(f"O valor sem desconto foi: {compra}")
    print(f"A compra com desconto ficou: {desconto5}")
          
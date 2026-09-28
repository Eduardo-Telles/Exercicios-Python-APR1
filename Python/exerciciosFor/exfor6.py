negativo=False
repeticao=0
qnt1=0
qnt2=0
qnt3=0
notas=0
soma=1
for repeticao in range (0,(negativo==False)):
    if repeticao>=0:
     nota= int(input("Digite uma nota"))
     if nota>0:
        if nota<4:
            qnt1+=1
            notas+=nota
        elif nota<6:
            qnt2+=1
            notas+=nota
        else:
            qnt3+=1
            notas+=nota
    else:
        negativo=True
        soma=qnt1+qnt2+qnt3
print(f"Quantia de notas menores que 4: {qnt1}")
print(f"Quantia de notas maiores que 4 e menores que 6: {qnt2}")
print(f"Quantia de notas maiores ou iguais a 6: {qnt3}")
print(f"A média de todas as notas é: {notas/soma}")

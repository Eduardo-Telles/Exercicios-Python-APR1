parou=False
listadenum=[]
lnegativos=[]
lpositivos=[]
numerador=0
qnt=0
pos=0
neg=0
i=0
while not parou:
    num=int(input("Digite um número quando quiser parar de adicionar numeros, digite 0 "))
    if num!=0:
        listadenum.append(num)
        qnt+=1
        numerador+=num
        if num>0:
            lpositivos.append(num)
            pos+=1
        else:
            lnegativos.append(num)
            neg+=1
    else:
        parou=True
porcentagempos=(len(lpositivos)/len(listadenum))*100
porcentagemneg=(len(lnegativos)/len(listadenum))*100
print(f"A média aritmética é {numerador/qnt}")
print(f"A quantidade de valores positivos é {pos} e os valores positivos são: {lpositivos}")
print(f"a quantidade de valores negativos é: {neg} e os valores negativos são: {lnegativos}")
print(f"O percentual de valores positivos é: {porcentagempos}% e a porcentagem de valores negativos é: {porcentagemneg}%")
print(f"A lista total dos numeros é: {listadenum}")




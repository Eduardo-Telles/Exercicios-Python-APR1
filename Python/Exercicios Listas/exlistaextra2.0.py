import random
loto = []
aposta = []
acertos = 0
i = 0
certos=[]
while i < 5:
    num = random.randint(0, 49)
    j = 0
    repetido = False
    while j < i:
        if loto[j] == num:
            repetido = True
        j += 1
    if repetido == False:
        loto.append(num)
        i += 1
print(loto)
while len(aposta)<10:
    num=int(input("Digite numeros para a aposta que sejam diferentes"))
    aposta.append(num)
print(aposta)
i=0
qnt=0
while i<10:
    x=0
    while x <5:
        if loto[x]==aposta[i]:
         acertos+=1
        x+=1
    i+=1
print(f"\nVoce acertou {acertos} números!")
sequencia=[]
i=0
while i < 4:
    num=int(input("Digite um número para a sequencia"))
    sequencia.append(num)
    print(sequencia)
    i+=1
if sequencia[0]==sequencia[2]:
    print("V")
elif sequencia[1]==sequencia[3]:
    print("V")
else:
    print("F")



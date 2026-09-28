C=int(input("Digite a capacidade da cabine"))
A=int(input("Digite o número de alunos"))
alunos=A
if C<2 or C>100 or A<1 or A>1000:
    print("Não é permitido")
else:
    i=0
    acabou=False
    while acabou==False:
        A=A-(C-1)
        i+=1
        if A<=0:
            print(f"O número mínimo de viagens para levar {alunos} alunos de teleférico é: {i}")
            acabou=True
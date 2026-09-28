lista=[]
parou=False
alunos=int(input("Digite a quantidade de alunos"))
soma=0
while not parou:
    notas=int(input("Digite notas"))
    soma=soma+notas 
    lista.append(notas)
    if soma >= 10*alunos:
        print(f"As notas foram: {lista}")
        print(f"A média aritmética foi: {soma/alunos}")
        parou==True



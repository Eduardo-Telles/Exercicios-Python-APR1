cont=True
soma=0
alunos=0
print("Digite as notas dos alunos, quando quiser parar a atividade digite um número negativo")
while cont==True:
    num=float(input("Digite uma nota "))
    if num>=0:
        soma=soma+num
        alunos=alunos+1
    else:
        cont=False
print(f"A média aritmética da turma foi: {soma/alunos}")

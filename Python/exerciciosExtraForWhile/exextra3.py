nota1=0
nota2=0
nita3=0
alunos=50
aluno=0
mediapond=0
geral=0
for alunos in range(1,51):
    nota1= int(input("Digite a nota1"))
    nota2= int(input("Digite a nota2"))
    nota3= int(input("Digite a nota3"))
    aluno=aluno+1
    mediapond=(nota1*2+nota2*3+nota3*5)/10
    geral=mediapond+geral
    if mediapond>=6:
        print(f"aluno {aluno} foi Aprovado e sua média foi= {mediapond}")
    else:
        print(f"aluno {aluno} foi Reprovado e sua média foi= {mediapond}")
print(f"A média geral da turma foi {geral/50}")
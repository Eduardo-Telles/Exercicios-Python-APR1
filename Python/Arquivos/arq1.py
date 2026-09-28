def existe_arquivo(nome):
    import os
    #verifica se o arquivo com nome informado existe
    if os.path.exists(nome):
        return True
    else:
        return False
def escrever_alunos(lista):
    #abre o arquivo para escrever
    arq=open("Dados_alunos.txt","w")
    for alu in range(len(lista)):
        aluno= ""
        for i in range(len(lista[alu])):
            aluno+=lista[alu][i]+';'
        aluno+='\n'
        arq.write(aluno)
    arq.close()
        
def main():
    alunos=[['João','BES','198372847'],['Maria','ADS','1232131873'],['Tevez','BES','169898989']]
    escrever_alunos(alunos)
#abre o aruivo para leitura
    if existe_arquivo("Dados_alunos.txt"):
        arq=open("Dados_alunos.txt","r")
        for linha in arq:
            linha=linha.split(";")
            print(f"Nome do aluno: {linha[0]}")
            print(f"Curso: {linha[1]}")
            print(f"Telefone: {linha[2]}")
        arq.close()
    else:
        print("Arquivo não encontrado!")
main()
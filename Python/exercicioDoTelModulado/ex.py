def criar_lista():
    nome=input("Nome do contato: ")
    contatos=[]
    while nome!="":
        pessoa=[]
        pessoa.append(nome)
        tel=input("Número de telefone ou celular: ")
        pessoa.append(tel)
        city=input("Informe a cidade: ")
        pessoa.append(city)
        contatos.append(pessoa)
        nome=input("Informe o nome de um novo contato ou digite enter para encerrar: ")
    return contatos

def imprimir_lista(lista):
    print("Agenda de contatos:")
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end="")
            if j==0:
                print(":", end=" ")
            elif j==1:
                print(",", end=" ")
            elif j==2:
                print()
    print()
        
def main():
    contatos=[]
    contatos=criar_lista()
    imprimir_lista(contatos)
main()
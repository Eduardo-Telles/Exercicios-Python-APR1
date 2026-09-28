agenda=[]#guarda todos os contatos
continua="sim"
while continua=="sim" or continua=="S" or continua=="s" or continua=="Sim":
    contato=[]#guarda o contato de uma pessoa
    nome=input("Informe um nome do contato")
    contato.append(nome)
    tel= input("Informe o telefone do contato")
    contato.append(tel)
    cidade=input("Informe a cidade do contato")
    contato.append(cidade)
    #inseri a lista de contato na lista agenda
    agenda.append(contato)
    continua= input("Digite sim(Sim) ou S(s) para inserir um novo contato ou digite enter para encerrar: ")
print("Agenda de Contatos")
for i in range(len(agenda)):
    print(f"{agenda[i][0]} - {agenda[i][1]}: {agenda[i][2]}")
agenda=[]#guarda todos os contatos
continua="sim"
while continua=="sim" or continua=="S" or continua=="s" or continua=="Sim":
    contato=[]#guarda o contato de uma pessoa
    nome=input("Informe um nome do contato")
    contato.append(nome)
    tel= input("Informe o telefone do contato")
    contato.append(tel)
    #inseri a lista de contato na lista agenda
    agenda.append(contato)
    continua= input("Digite sim(Sim) ou S(s) para inserir um novo contato ou digite enter para encerrar: ")
print(agenda)
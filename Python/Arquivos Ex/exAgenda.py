def existe_arquivo(nome):
    import os
    #verifica se o arquivo com nome informado existe
    if os.path.exists(nome):
        return True
    else:
        return False


def carregar_dados_arquivos(Agenda):
    if existe_arquivo("Agenda_contatos.txt"):
        arq= open("Agenda_contatos.txt","r")
        for linha in arq:
            contato=[]
            linha=linha.split(';')
            telefones=linha[1].split('_')
            #inseri o nd(linha[0])
            #inseri cada telefone
            contato.append(telefones)
            #inseri cidadeome do contato
            contato.append
            contato.append(linha[2])
            #inseri um novo contato em agenda
            Agenda.append(contato)


def main():
    Agenda=[['Elaine',['1687979999'],'Ibaté'],['Edmara',['1798989899','14657657657'],'Bauru']]
    #carregar dados do arquivo
    carregar_dados_arquivos(Agenda)
    #opçoes do menu
    
main()
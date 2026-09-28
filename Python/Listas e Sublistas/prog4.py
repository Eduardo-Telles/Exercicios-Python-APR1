#1-Inserir Contato
#2-Buscar Contato
#3-Inserir um novo telefone em um conato já existente
#4-Excluir um contato da agenda
#5-Imprimir todos os Contatos
agenda=[]
novaagenda=[]
cont="s"
while cont=="Sim" or cont=="S" or cont=="sim" or cont=="s":
    menu=int(input("Digite um número negativo para parar, Digite 0 para adicionar um contato, Digite 1 para buscar um contato, Digite 2 para inserir um tel em um contato existente, Digite 3 para excluir um contato da agenda, Digite 4 para imprimir todos os contatos"))
    achou=False
    contatoadd=False
    buscar=False
    teladd=False
    excl=False
    imprimir=False
    if menu==0:
        contatoadd=True
    elif menu==1:
        buscar=True
    elif menu==2:
        teladd=True
    elif menu==3:
        excl=True
    elif menu==4:
        imprimir=True
    else:
        cont="n"
    while contatoadd==True:
        contato=[]
        nome=input("Digite um nome")
        contato.append(nome)
        tel=input("Digite um telefone")
        contato.append(tel)
        agenda.append(contato)
        contatoadd=False
#busca
    while buscar==True:
        busca=input("Busque um contato")
        i=0
        while achou==False:
            if i<=len(agenda)-1:
                j=0
                while j<len(agenda[i]):
                    if busca==agenda[i][j]:
                        print(f"encontrou: {busca}")
                        achou=True
                        buscar=False   
                    j+=1
                i+=1
            else:
                print(f"Não encontrado")
                achou=True
                buscar=False
#inserir tel em contato existente
    while teladd==True:
        busca=input("Digite um contato")
        i=0
        while achou==False:
            if i<=len(agenda)-1:
                j=0
                while j<len(agenda[i]):
                    if busca==agenda[i][j]:
                        tel=input("Digite um telefone")
                        agenda[i].append(tel)  
                        teladd=False
                        achou=True
                        print(f"A agenda nova é: {agenda}")
                    j+=1
                i+=1
            else:
                print(f"Não encontrado")
                achou=True
                teladd=False
#Excluir contato da agenda
    while excl==True:
        busca=input("Digite um contato")
        i=0
        while achou==False:
            novaagenda=[]
            if i<=len(agenda)-1:
                j=0
                while achou==False and j<len(agenda[i]):
                    if busca==agenda[i][j]:
                        excl=False
                        achou=True
                        for x in agenda:
                            if x != agenda[i]:
                                novaagenda=novaagenda+[x]
                        agenda=novaagenda
                        print(f"A agenda nova é: {agenda}")  
                    j+=1
                i+=1
            else:
                print(f"Não encontrado")
                achou=True
                excl=False
#Imprimir todos os contatos
    while imprimir==True:
        print(f"A agenda é: {agenda}")
        imprimir=False
    
        

            
              



        

        
    
    
    
    

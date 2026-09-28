contatos = [["Pedrinho", "14 999999999"], ["Juca",
"17 922999897"], ["Paula", "16 31239718"],
["Aurora", "16 81125569"]]
print(contatos[2][1])
nome=input("Digite o contato que deseja: ")
i=0
achou=False
while i<len(contatos):
    if nome==contatos[i][0]:
        achou=True
        print(f"Telefone da (o) {nome} é {contatos[i][1]}")
    i+=1
if not achou:
    print("Conato não localizado")


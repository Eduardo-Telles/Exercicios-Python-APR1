LE=[]
LPU=[]
num=int(input("Digite 1 para add paciente em Emergência ou Urgência, Digite 2 para add paciente pouco Urgente ou não Urgente, Digite 3 para atender paciente E ou U, Digite 4 para atender paciente PU ou NU"))
i=1
if num==1:
    while i>0:
        i=int(input("Digite o numero do paciente que quer inserir, caso acabe os pacientes E e U digite 0!!!"))
        if i>0:
            LE.append(f"P{i}")
print(f"Fila dos pacientes E e U: {LE}")
i=1
if num==2:
    while i>0:
        i=int(input("Digite o numero do paciente que quer inserir, caso acabe os pacientes PU e NU digite 0!!!"))
        if i>0:
            LPU.append(f"P{i}")
print(f"Fila dos pacientes PU e NU: {LPU}")




print("Tabela ASCII de 32 a 127: ")
for i in range(32,128,3):
    print(f"ASCII[{i}] = {chr(i)} | ASCII[{i+1}] = {chr(i+1)} | ASCII[{i+2}] = {chr(i+2)}")
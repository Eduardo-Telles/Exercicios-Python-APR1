def entrada():
    palavra=input("Digite uma palavra: ")
    return palavra
def qntdcaracteres(palavra,letras):
    if letras == len(palavra):
        return letras
    if len(palavra)==0:
        return letras
    elif letras < len(palavra):
        return qntdcaracteres(palavra,letras+1)
    
def main():
    palavra=entrada()
    letras=0
    resultado=qntdcaracteres(palavra,letras)
    print(f"A qntd de caracteres da str {palavra} é {resultado}")
main()
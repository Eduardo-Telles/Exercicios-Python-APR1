#função menu
def menu():
    print("1. somar")
    print("2. Dividir")
    print("3. Subtrair")
    print("4. Multiplicar")
    print("5. Percentual")
    print("6. Sair")
    opc=int(input("Escolha uma opção entre 1 e 6: "))
    return opc

def entrada():
    num=float(input("Informe o valor"))
    return num

def somar(n1,n2):
    return n1 + n2

def divisão(n1,n2):
    return n1 / n2

def subtrair(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def calcular_percentual(n1,perc):
    return n1*(perc/100)
#ou
def calcular_percentual_chamandooutrafuncao(valor,perc):
    prod=multiplicacao(valor,perc)
    dividir=divisão(prod,100)
    return dividir
#Programa Principal
print("Programa da calculadora")
#Chamada da função que apresenta o menu de opções
opcao=1
while opcao !=6:
    opcao = menu() #opção guarda o valor retornado pela função
    if opcao==1:
        #chamada da função que obtém os dados de entrada
        n1= entrada()
        n2= entrada()
        result = somar(n1,n2)
        print(f"Resultado da soma: {result}")
    elif opcao==2:
        n1= entrada()
        n2= entrada()
        if n2==0:
            print("Não existe divisão por zero!")
        else:
            #chamada da função divisão
            print(f"O resultado da divisão é: {divisão(n1,n2)}")
    elif opcao==3:
        n1= entrada()
        n2= entrada()
        print(f"O resultado da subtração: {subtrair(n1,n2)}")
    elif opcao==4:
        n1=entrada()
        n2=entrada()
        print(f"O resultado da multiplicação: {multiplicacao(n1,n2)}")
    elif opcao==5:
        n1=entrada()
        perc=entrada()
        result= calcular_percentual_chamandooutrafuncao(n1,perc)
        print(f"O resultado da porcentagem: {result}")
    else:
        print("Opção Inválida")
    





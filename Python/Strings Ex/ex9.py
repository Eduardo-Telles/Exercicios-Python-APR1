def entrada():
    string=input("Entre com uma string: ")
    return string
def contar_caracteres(string,caractere):
    cont=0
    for i in range(len(string)):
        if string[i] == caractere:
            cont+=1
    return cont
def verificar_anagrama(str1,str2):
    #remove os espaços em branco
    str1=str1.replace(" ","")
    str2=str2.replace(" ","")
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            #verifica quantas vezes o caractere de str1[i] apareceu
            tot_str1=contar_caracteres(str1,str1[i])
            tot_str2=contar_caracteres(str2,str1[i])
            if tot_str1!=tot_str2:
                return False
        return True
        
def main():
    palavra1= entrada().lower()
    palavra2= entrada().lower()
    anagrama=verificar_anagrama(palavra1,palavra2)
    if anagrama==True:
        print(f"{palavra1} e {palavra2} são um anagrama!")
    else:
        print(f"{palavra1} e {palavra2} não são um anagrama!")

main()
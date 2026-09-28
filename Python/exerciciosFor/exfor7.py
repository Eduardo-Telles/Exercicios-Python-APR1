proximo=1
atual=0
for i in range (8):
    if i==0:
        print(atual)
    elif i == 1:
        print(proximo)
    else:
        c= atual+proximo
        print(c)
        atual=proximo
        proximo=c   

      

    
   



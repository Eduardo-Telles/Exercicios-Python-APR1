contador=0
numero=2
while contador<20:
    primo=True

    for i in range(2,numero):
        if numero%i==0:
            primo=False
    if primo:
        print(numero)
        contador+=1
    numero+=1
 
    
    
    
  

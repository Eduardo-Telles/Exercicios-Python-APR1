''' Crie um algoritmo para resolver equações do 2º grau. 
Considere:
ax2 + bx + c = 0   (a deve ser diferente de 0)
delta = b2 - 4 * a * c 
Caso: delta < 0, não existe raiz real
    delta = 0, existe uma raiz real:  x = (-b) / (2 * a)
          delta > 0, existem duas raízes reais:
x1 = (- b + raiz quadrada de delta) / (2 * a)
x2 = (- b - raiz quadrada de delta) / (2 * a)'''
a = float(input("Digite um valor para a"))
b = float(input("Digite um valor para b"))
c = float(input("Digite um valor para c"))
delta = (b**2) -4 * a * c
x = (-b) / (2*a)
x1 = (-b + (delta**0.5)) / (2*a)
x2 = (-b - (delta**0.5)) / (2*a)
if a == 0:
    print(f"Valor não permitido")
elif delta < 0:
    print(f"Não existe raiz real")
elif delta == 0:
    print(f"existe uma raiz real {x}")
elif delta > 0:
    print(f"existem duas raízes reais {x1} and {x2}")
     
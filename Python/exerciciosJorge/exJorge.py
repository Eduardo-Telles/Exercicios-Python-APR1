memoria=0
x=1
while x>=0:
    x=int(input("Digite um número"))
    if x>memoria:
        memoria= x
print(f"O maior número entre eles é: {memoria}")
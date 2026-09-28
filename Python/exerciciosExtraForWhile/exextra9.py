qnt=0
num=0
Lperf=[]
soma=0
while qnt<5:
    num+=1
    div=1
    soma=0
    while num>div:
        if num%div==0 and num!=div:
                soma+=div
                if soma==num:
                    Lperf.append(num)
                    qnt+=1
        div+=1
print(Lperf)
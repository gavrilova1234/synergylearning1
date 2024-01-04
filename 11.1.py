def fact(x):
    p=1
    for i in range(2,x+1):
        p=p*i
    return p
n=int(input("Введите число: "))
sp=[]
for j in range(n,0,-1):
    sp.append(fact(j))
print(sp)

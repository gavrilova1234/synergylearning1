print ("Введите последовательность чисел")
sp=list(map(int,input().split()))
l=len(sp)
for i in range(l):
    k=sp.count(sp[i])
    if k==1: print("NO")
    else: print("YES")
    

N=int(input("Количество элементов в  списке: "))
sp=list(map(int,input().split(maxsplit=N-1)))
mn=set(sp)
l=len(mn)
print ("Количество различных элементов:",l)




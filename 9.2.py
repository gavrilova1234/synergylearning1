N1=int(input("Количество элементов в певом списке: "))
sp1=list(map(int,input().split(maxsplit=N1-1)))
N2=int(input("Количество элементов во втором списке: "))
sp2=list(map(int,input().split(maxsplit=N2-1)))             
mn1=set(sp1)
mn2=set(sp2)             
mn=mn1&mn2
l=len(mn)
print ("Повторяющиеся элементы", *mn)
print ("Количество повторяющиеся элементов: ",l)




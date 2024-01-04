m=int(input("Введите вместимось лодки: "))
k=int(input("Введите количество рыбаков: "))
a=[]
print ("Введите вес каждого рыбака")
for i in range(k):
    a.append(int(input()))
r=0 # количество рыбаков
x=min(a)
t=a.index(x)# индекс самого легкого рыбака
if 2*min(a)<=m:
        for i in range(k):
            if i!=t:
                if x+a[i]<=m:
                    r=r+1 # количество рыбаков, перевезенных самым легким из них
if 2*min(a)<=m: l=k-r
else: l=k
print("Количество лодок:",l)


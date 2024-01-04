N=int(input("Введите количество чисел: "))
k=0
for i in range(1,N+1):
    print (i, "число: ")
    a=int(input())
    if a==0: k=k+1
print ("Количество введенных нулей: ",k)


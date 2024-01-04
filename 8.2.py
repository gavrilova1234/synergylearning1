N=int(input("Введите размерность массива N: "))
print ("Введите ", N, "чисел в одну строку")
spisok=list(map(int,input().split()))
spisok1=[]
a=spisok[N-1]
for i in range(1,N):
    spisok1.append(spisok[i-1])

spisok1.insert(0,a)    

print ('Перевернутый список', *spisok1)

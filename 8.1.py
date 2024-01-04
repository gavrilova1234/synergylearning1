N=int(input("Введите размерность массива N: "))
print ("Введите ", N, "чисел")
spisok=[]
for i in range(N):
    a=int(input())
    spisok.append(a)
print ('Начальный список', *spisok)
spisok.reverse()
print ('Перевернутый список', *spisok)


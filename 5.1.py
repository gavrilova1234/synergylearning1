a=int(input("Введите число: "))
if a==0:
    print("Нулевое число")
elif a>0:
    if a%2==0:
        print("Положительное четное число")
    else:
        print ("Число не является четным")
        print("Положительное нечетное число")
else:
    if a%2==0:
        print("Отрицательное четное число")
    else:
        print ("Число не является четным")
        print("Отрицательное нечетное число")
    
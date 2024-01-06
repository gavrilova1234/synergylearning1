print ('Введите количество элементов массива')
n = int(input())
a = []
print ('Введите элементы массива')
for i in range(n):
    b = int(input())
    a.append(b)
print('Массив:', a)
for i in range(n):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print('Массив отсортированный:', a)
c = len(set(a))
print('Количество различных элементов:',c)

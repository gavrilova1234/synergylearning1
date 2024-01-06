def cmp(x):
    return x % 3
print ('Введите количество элементов массива')
n = int(input())
a = []
print ('Введите элементы массива')
for i in range(n):
    b = int(input())
    a.append(b)
a.sort(key=cmp)
print(a)

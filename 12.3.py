print ('Введите количество сотрудников')
n = int(input())
sph = []
print ('Введите сколько сотрудник получает за час')
for i in range(n):
    b = int(input())
    sph.append(b)
hs = []
print ('Введите сколько сотрудник отработал часов')
for i in range(n):
    c = int(input())
    hs.append(c)
res = []
for i in range(n):
    r = sph[i] * hs[i] 
    res.append(r)
res.sort()
print (res)

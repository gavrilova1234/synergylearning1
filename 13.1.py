import random
def pr(x):
    for i in x:
        print(*i)
m1=[[0 for a in range (10)] for b in range (10)]
m2=[[0 for a in range (10)] for b in range (10)]
m=[[0 for a in range (10)] for b in range (10)]
for i in range(10):
    for j in range (10):
        m1[i][j]=random.randint(0, 99)
print("1 матрица")
pr(m1)
print("") 
for i in range(10):
    for j in range (10):
        m2[i][j]=random.randint(0, 99)
print("2 матрица")   
pr(m2)
print("")
for i in range(10):
    for j in range (10):
        m[i][j]= m1[i][j]+ m2[i][j]
print("Резултирующая матрица")   
pr(m)

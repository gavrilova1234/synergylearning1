slovo = (input("Введите слово строчными английскими буквами: ")) 
a = slovo.count('a')
e = slovo.count('e')
i = slovo.count('i')
o = slovo.count('o')
u = slovo.count('u')
print("В слове",slovo,"количество гласных букв")
if a>0:
    print("a - ",a)
else:
    print("a - False")
if e>0:
     print("e - ",e)
else:
    print("e - False")
if i>0:
     print("i - ",i)
else:
    print("i - False")
if o>0:
     print("o - ",o)
else:
    print("o - False")
if u>0:
     print("u - ",u)
else:
    print("u - False")
l=len(slovo)
k=l-(a+e+i+o+u)
print("Количество согласных букв -",k)


    

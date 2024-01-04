import collections
pets = {
    1:{ "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"}},
    2:{"Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"}},
    3:{"Буся": {
                "Вид питомца": "кошка",
                "Возраст питомца": 14,
                "Имя владельца": "Татьяна"}}}
def pets_list():
    last = collections.deque(pets, maxlen=1)[0]
    print ("На данный момент в базе находятся следующие питомцы")
    for ID in range(1,last+1,):
       if ID in pets.keys():
            kl1=pets[ID]
            kl=str(kl1)
            a=kl.index("'")
            b=kl.index(":")
            c=kl[a+1:b-1]
            g=pets[ID][c]['Возраст питомца']
            g1=str(g)
            g2=int(g1)
            print(ID,":", pets[ID][c]["Вид питомца"], "по кличке",c,". Возраст питомца:", pets[ID][c]['Возраст питомца'],get_suffix(g2),
            "Имя владельца:",  pets[ID][c]['Имя владельца'])
    
def get_pet(id):
    return pets[id] if id in pets.keys() else False   
    
def create():
    last = collections.deque(pets, maxlen=1)[0]
    n=last+1
    k=input("Имя питомца: ")
    k1=input("Вид питомца: ")
    k2=int(input("Возраст питомца: "))
    k3=input("Имя владельца:  ")
    pets[n]={k:{"Вид питомца": k1,
            "Возраст питомца": k2,
            "Имя владельца": k3}}
def read():
    id=int(input("Введите ID питомца: "))
    # из словаря выделяю кличку животного
    print(get_pet(id))
    if id in pets.keys():
        kl1=pets[id]
        kl=str(kl1)
        a=kl.index("'")
        b=kl.index(":")
        c=kl[a+1:b-1]
        g=pets[id][c]['Возраст питомца']
        g1=str(g)
        g2=int(g1)
        print(get_suffix(g2))
        print("Это", pets[id][c]["Вид питомца"], "по кличке",c,". Возраст питомца:", pets[id][c]['Возраст питомца'],get_suffix(g2),
        "Имя владельца:",  pets[id][c]['Имя владельца'])
def delete():
    print("Удаление питомца из базы")
    id=int(input("Введите ID питомца: "))
    print(get_pet(id))
    if id in pets.keys():
         del pets[id]
    print ("Оставшиеся ID животных", pets.keys())

def update():
    print("Изменение информации о питомце в базе") 
    id=int(input("Введите ID питомца: "))
    print(get_pet(id))
    if id in pets.keys():
        z=input("Имя питомца: ")
        z1=input("Вид питомца: ")
        z2=int(input("Возраст питомца: "))
        z3=input("Имя владельца:  ")
        pets[id]={z:{"Вид питомца": z1, "Возраст питомца": z2, "Имя владельца": z3}}
def get_suffix(age):# функция, с помощью которой можно получить суффикс# 'год', 'года', 'лет'#
    year = ''
    if (age % 10 == 1) and (age != 11) and (age % 100 != 11):
        year = 'год'
    elif (1 < age % 10 <= 4) and (age != 12) and (age != 13) and (age != 14):
        year = 'года'
    else:
        year = 'лет'
    return year
command=input("Выберите одну из команд: create, read, delete или update , для завершения - stop: ")
while command !='stop':
    print("")
    if command=="create": create()
    elif command=="read": read()
    elif command=="delete":delete()
    elif command=="update": update()
    else: print("Неправильно набрана команда")
    print("")
    command=input("Выберите одну из команд: create, read, delete или update , для завершения - stop: ")
    
print("Работа с базой завершена")
pets_list()


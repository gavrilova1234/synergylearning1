pets ={}
pets1={}
k=input("Имя питомца: ")
k1=input('Вид питомца: ')
k2=int(input('Возраст питомца: '))
if (k2 % 10 == 1) and (k2 != 11) and (k2 % 100 != 11):
    god='год'
elif (1 < k2 % 10 <= 4) and (k2 != 12) and (k2 != 13) and (k2 != 14):
    god = 'года'
else:
    god = 'лет'
k3=input('Имя владельца:  ')
pets2={'Вид питомца:':k1, 'Возраст питомца:':k2, 'Имя владельца:':k3  }
pets[k]=pets2
print("Это ", pets2['Вид питомца:'], " по кличке ",*pets.keys(),". Возраст питомца: ", pets2['Возраст питомца:']," ", god,  ". Имя владельца: ", pets2['Имя владельца:'],sep="")
   

x=int(input("Минимальная сумма инвестиций: "))
a=int(input("Количество денег у Майкла: "))
b=int(input("Количество денег у Ивана: "))
if a>=x:
    if b>=x:
        print (2)
    else:
        print ("Mike") 
else:
    if b>=x:
      print ("Ivan")
    elif a+b>=x:
      print (1)
    else:
      print (0)
      

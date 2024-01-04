class cassa:
   
    def __init__(self, summ):
        self.summ = summ

    def op_up(self,x):
        self.summ +=x
        return print(f"На данный момент в кассе {self.summ} руб.")
    def count_1000(self):
        t= self.summ//1000
        return print(f"Количество цедых тысяч в кассе {t}")
    def ake_away (self,x):
        if x<self.summ:
            print(f"В кассе осталось {self.summ-x} руб.")
        else:
            print ("Hедостаточно денег")
            
s=int(input("Сумма денег в кассе "))
s1=cassa(s)
print(s1.summ)
pr=int(input("Сумма денег в кассе увкличилась на "))
s1.op_up(pr)
s1.count_1000()
sd=int(input("Сумма денег, которую нужно отдать "))
s1.ake_away(sd)
        

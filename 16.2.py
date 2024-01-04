class cherepaxa:
   
    def __init__(self,x, y, s,x2,y2):
        self.x=x
        self.y=y
        self.s=s
        self.x2=x2
        self.y2=y2

    # метод: увеличивает y на s
    def go_up(self,s):
        self.y += self.s
        print("Новая координата y+: ", self.y)
        
    # метод: уменьшает y на s
    def go_down(self,s):
        self.y -= self.s
        print("Новая координата y-: ", self.y)

    # метод: увеличивает x на s
    def go_left(self,s):
       self.x += self.s
       print("Новая координата x+: ", self.x)

    # метод: уменьшает x на s
    def go_right(self,s):
        self.x -= self.s
        print("Новая координата x-: ", self.x)

    # метод: увеличивает s на 1
    def evolve(self,s):
        self.s +=1
        print("Новое значение s+: ", self.s)

    # метод: уменьшает s на 1
    def degrade(self,s):
        if self.s-1>0:
            s -=1
        else: print ("Уменьшить значение s нельзя")

    def ount_moves(self, x2, y2):
        print("Минимальное количество действий: ", int((self.x2-self.x)/self.s + (self.y2-self.y)/self.s))
        
x1,y1=map(int,(input("начальные координаты черепахи: x, y ")).split())
s1=int(input("количество клеточек, на которое ерепаха перемещается за ход "))
x3,y3=map(int,(input("конечные координаты черепахи: x, y ")).split())
ch=cherepaxa(x1,y1,s1,x3,y3)
ch.go_up(s1)
ch.go_down(s1)
ch.go_left(s1)
ch.go_right(s1)
ch.evolve(s1)
ch.degrade(s1)
ch.ount_moves(x3,y3)

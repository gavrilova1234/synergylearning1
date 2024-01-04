class Transport:
    def __init__(self, name, max_speed, mileages):
        self.name = name
        self.max_speed = max_speed
        self.mileages = mileages
    def seating_capacity(self, capacity):
        return print(f"Вместимость одного автобуса {self.name}: {capacity} пассажиров")
class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return super ().seating_capacity (capacity = 50)

Auto1 = Autobus("Renaul Logan", 180,12)
Auto1.seating_capacity()

class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.__maxspeed = maxspeed
    def print(self):
        print('Color :',self.color)
        print('Maxspeed :',self.__maxspeed)

class Car(Vehicle):

    def __init__(self,color,maxspeed,gears,iscompactable):
        super().__init__(color,maxspeed)
        self.gears = gears
        self.iscompactable = iscompactable

    def printCar(self):
        super().print()
        print('Gears :',self.gears)
        print('IScompactable :',self.iscompactable)

c = Car('Red',100,3,True)
c.printCar()
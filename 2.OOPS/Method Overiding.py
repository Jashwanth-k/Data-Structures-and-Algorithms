class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.__maxspeed = maxspeed
    def print(self):
        print('Color :',self.color)
        print('Maxspeed :',self.__maxspeed)

class Car(Vehicle):
    def __init__(self,color,maxspeed,gears,iscompact):
        super().__init__(color,maxspeed)
        self.gears = gears
        self.iscompact = iscompact

    def print(self):
        super().print()
        print('Gears :',self.gears)
        print('IScompact :',self.iscompact)

c = Car('Green',100,4,True)
c.print()

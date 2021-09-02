class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self._maxspeed = maxspeed

    def print(self):
        print('Color :',self.color)
        print('Maxspeed :',self._maxspeed)   #protected members are denoted by single underscore

class Car(Vehicle):
    def __init__(self,color,maxspeed,gears,isconvertable):
        super().__init__(color,maxspeed)
        self.gears = gears
        self.isconvertable = isconvertable

    def print(self):
        #super().print()
        print('MAXSPEED :',self._maxspeed)   #PM are like public members but can be accessed outside a function
        print('GEARS :',self.gears)
        print('ISCONVERTABLE :',self.isconvertable)

c = Car('Red',100,3,True)
c.print()
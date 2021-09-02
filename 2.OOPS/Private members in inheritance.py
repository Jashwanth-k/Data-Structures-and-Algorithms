class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.__maxspeed = maxspeed
    def GetMaxspeed(self):  #Through GetMaxspeed we can access the private member [self.__maxspeed]
        return self.__maxspeed

class Car(Vehicle):

    def __init__(self,color,maxspeed,gears,iscompactable):
        super().__init__(color,maxspeed)
        self.gears = gears
        self.iscompactable = iscompactable

    def printCar(self):
        print('Color :',self.color)
        print('Speed :',self.GetMaxspeed())
        print('Gears :',self.gears)
        print('IScompactable :',self.iscompactable)

c = Car('Red',100,3,True)
c.printCar()
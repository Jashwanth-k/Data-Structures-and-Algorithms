class Vehicle:
    def __init__(self,color,company):
        self.color = color
        self.company = company

class Car(Vehicle):

    def __init__(self,color,company,gears,iscompactable):
        super().__init__(color,company)
        self.gears = gears
        self.iscompactable = iscompactable

    def printCar(self):
        print('Color :',self.color)
        print('Company :',self.company)
        print('Gears :',self.gears)
        print('IScompactable :',self.iscompactable)

c = Car('Red','Honda',3,True)
c.printCar()
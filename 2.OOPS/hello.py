class Mother:
    def print(self):
        print('Print from mother called')

class Father:
    def print(self):
        print('Print from father called')

class Child(Father,Mother):
    def __init__(self,name):
        self.name = name
    def Childprint(self):
        print('The child name is :',self.name)

c = Child('rohan')
c.print()

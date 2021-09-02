class Mother:
    def __init__(self):
        self.name = 'ninja'
    def print(self):
        print('The print from Mother')

class Father:
    def __init__(self):
        self.name = 'ZX10r'
    def print(self):
        print('The print from Father')

class Child(Mother,Father):
    def __init__(self):
        super().__init__()
    def ChildPrint(self):
        print('The name of child is :',self.name)

c = Child()
c.ChildPrint()
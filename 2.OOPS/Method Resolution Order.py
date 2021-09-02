class Mother:
    def __init__(self):
        self.name = 'ninja'

    def print(self):
        print('Print from mother class')

class Father:
    def __init__(self):
        self.name = 'ZX10r'

    def print(self):
        print('Print from father class')

class Child(Mother,Father):
    def __init__(self):
        super().__init__()
    def print(self):
        print('The name of child :',self.name)

c = Child()
c.print()
print(Child.mro())  # by this fun we can check inheritance order
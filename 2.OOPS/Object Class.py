class Circle(object):
    def __init__(self,radius):
        self.radius = radius

    def __str__(self):  # with this fun we can print about the class object
        return 'This Circle object takes radius as an argument'

c = Circle(3)
print(c)
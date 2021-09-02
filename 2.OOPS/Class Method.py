from datetime import date
class student:
    def __init__(self,name,age=15,percentage=50):
        self.name = name
        self.age = age
        self.percentage = percentage

    @classmethod
    def fromBirthYear(cls,name,year,percentage):
        return cls(name,date.today().year-year,percentage)

    def studentDetails(self):
        print('Name = ',self.name)
        print('age =',self.age)
        print('percentage =',self.percentage)

s1 = student('jashwanth')
s1 = student.fromBirthYear('jashwanth',2001,75)
s1.studentDetails()

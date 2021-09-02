class student:
    passpercentage = 50
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def StudentDetails(self):
        print(self.__name)
        print(self.age)

s1 = student('jashwanth',19)
s1.StudentDetails()
print(s1._student__name)   #using python manglin we can access private variables syntax : object_class__variable

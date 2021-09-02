class student:
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber

s1 = student('priya',32)
s2 = student('ninja',34)

print(s1.__dict__)
print(s2.__dict__)
class student:
    name = 'jashwanth'
    def storedetails(self):
        self.age = 24
    def printdetails(self):
        print(self.name)
        print(self.age)

    @staticmethod     # for staticmethod we should method @staticmethod decorator before the function
    def welcome_to_school():
        print('Hey! welcome to school')

s = student()
s.storedetails()
s.printdetails()
s.welcome_to_school()
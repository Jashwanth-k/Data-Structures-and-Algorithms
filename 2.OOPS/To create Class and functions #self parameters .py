class student:
    passingpercentage = 40

    def studentDetails(self):
        self.name = 'jashwanth'
        print('student name is =', self.name)
        self.percentage = 80
        print('student percentage is =', self.percentage)

    def ispassed(self):
        if self.percentage > student.passingpercentage:
            print('student is passed')
        else:
            print('student is not passed')


s1 = student()
s1.studentDetails()
s1.ispassed()

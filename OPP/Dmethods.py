#accessor and mutator

class Students:
    def getName(self):
        return self.name
    def setName(self, name):
        self.name= name

    def getMarks(self):
        return self.marks
    def setMarks(self, marks):
        self.marks = marks


p = int(input("How many Students?"))

i=0

while i < p:
    s = Students()
    name = input("enter your name")
    s.setName(name)
    marks = int(input("Enter marks"))
    s.setMarks(marks)
    print("===========")
    print("The grade of {} is {}".format(s.getName(), s.getMarks()))
    print("===========")
    i=i+1


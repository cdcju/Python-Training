#example of inner class 
class Person:
    def __init__(self):
        self.name = "Agniswar"
        self.db = self.Dob()
    def display(self):
        print("Name = ", self.name)


    class Dob:
        def __init__(self):
            self.dd= 22
            self.mm=10
            self.yy = 1984
        def display(self):
            print("Date of birth is {}/{}/{}".format(self.dd,self.mm,self.yy))


p = Person()
p.display()
x = p.db
x.display()

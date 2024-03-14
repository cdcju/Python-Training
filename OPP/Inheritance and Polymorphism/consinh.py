#access the super class contstractor

class A:
    def __init__(self, property=0):
        self.property = property

    def display(self):
        print("The property of class A", self.property)

class B(A):
    def __init__(self, property1=0 , property=0):
        super().__init__(property)
        self.property1 = property1

    def display(self):
        print("property of class b is {} and a is {}".format(self.property1, self.property))


b = B(5000, 6000)

b.display()
#Private variables in python

class Myclass:
    def __init__(self):
        self.x=1  # x is  a public variable
        self.__y =3 # y is private variable

    def display(self):
        print(self.x)
        print(self._Myclass__y) #syntax to understand     


m = Myclass()
m.display()
class Father:
    def height(self):
        print("the height is 6.0ft")

class Mother:
    def color(self):
        print("The color is brown")


class Child(Father, Mother):
    pass

c = Child()
c.height()
c.color()


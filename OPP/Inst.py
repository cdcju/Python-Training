#understanding the instance variable

class Sample:
    def __init__(self):
        self.x =10

    def modify(self):
        self.x = self.x +10


s1 = Sample()
s2 = Sample()

print("Value of x in s1" , s1.x)
print("Value of x in s2" , s2.x)

s1.modify()
print("=====After Modification=======")
print("Value of x in s1" , s1.x)
print("Value of x in s2" , s2.x)
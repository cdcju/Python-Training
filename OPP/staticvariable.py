#Example of Static variable

class Sample:
    x=10
    @classmethod
    def modify(cls):
        cls.x+=10

s1 = Sample()
s2 = Sample()

print("Value of x in s1" , s1.x)
print("Value of x in s2" , s2.x)

s1.modify() # acting on the class variable
print("=====After Modification=======")
print("Value of x in s1" , s1.x)
print("Value of x in s2" , s2.x)

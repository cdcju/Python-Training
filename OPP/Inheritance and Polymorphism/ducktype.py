#duck typing philosophy

class A:
    def display(self):
        print("Hi i am A")


class B:
    def display(self):
        print("Hi i am B")


def call_dis(obj):
    obj.display()

a = A()
call_dis(a)

a = B()
call_dis(a)

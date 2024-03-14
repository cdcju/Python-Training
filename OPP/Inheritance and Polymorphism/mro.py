class A(object):
    def method(self):
        print("class A method")
        super().method()

class B(object):
      def method(self):
        print("class B method")
        super().method()  

class C(object):
    def method(self):
        print("class C method")

class X(A,B):
    def method(self):
        print("class X method")
        super().method() 


class Y(B,C):
    def method(self):
        print("class Y method")
        super().method() 


class P(X,Y, C):
    def method(self):
        print("class P method")
        super().method() 

p = P()
p.method()

            

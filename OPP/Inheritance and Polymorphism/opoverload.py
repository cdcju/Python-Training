#operator overload

class Book1:
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages


class Book2:
    def __init__(self, pages):
        self.pages = pages

a = Book1(150)
b = Book2 (750)

if(a>b):
    print("Book1 has more pages")
else:
    print("Book2 has more pages")


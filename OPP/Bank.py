class Bank():
    def __init__(self, accno , name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance
        self.__loan = 2000
    def display_to_an_employee(self):
            print(self.accno)
            print(self.name)
            print(self.balance)

b = Bank("SBI0033256", "Agniswar" ,10000 )
b.display_to_an_employee()
#b.__loan  # as it will create an error





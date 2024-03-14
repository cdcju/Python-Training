#example of single inheritance

class Bank():
    deposit = 100000
    @classmethod
    def cash_hand(cls):
        print(cls.deposit)

class Pnb(Bank):
    pass

class Sbi(Bank):
    cash = 150000
    @classmethod
    def cash_hand(cls):
        print(cls.cash + Bank.deposit)

a = Pnb()
a.cash_hand()

s = Sbi()
s.cash_hand()
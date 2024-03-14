class MyException(Exception):
    def __init__(self, arg):
        self.msg = arg



def check(dict):
    for k,v in dict.items():
        print("Name= {} and balance is {}".format(k,v))
        if(v <2000.00):
            raise MyException("Not enough balance in {} account".format(k))

bank = {'Ajay' : 6000.00, 'Bijay': 7000.00 , "kamal" : 1900}

try:
    check(bank)
except MyException as me:
    print(me)    



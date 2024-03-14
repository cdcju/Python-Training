# A simple function

def add():
    """ A function to add numbers """
    a=15.6
    b=23.6
    print("The sum is", a+b)


add()

# odd even checking

def odd_even(num):
    """ A function to check odd or even """
    if num%2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))    

    
odd_even(56)


# afunction with multiple return
def employee():
    name = "Agniswar"
    id2 = "ABCD-002"
    return name, id2


n, i = employee()
print("Name of the employee is :" , n)
print("\nID code of the employee is :" , i)


# Define a function in a function
def message(str):
    def display():
        return "How are you "
    result = display() + str
    return result

print(message("Agniswar"))        


# mody and location

def modify(x):
    x=15
    print(x, id(x))


x =10
modify(x)
print(x, id(x))


#keywords argument

def goods(item , price):
    print("Item : ", item)
    print("\nPrice :" , price)


goods(item = 'Sugar', price= 90.36)
goods(price= 36.36, item = "Abcd")


#variable length argument

def add2(fixed , *args):
    print("the fixed argument is", fixed)
    sum = 0
    for i in args:
        sum = sum +i
    print("The sum is :" , sum+fixed)    


add2(5+69+56+98+3+4+7)


# default value of a function

def our_sum(a =40, b=37):
    print("The sum is ", a+b)


our_sum()
our_sum(63)
our_sum(a=63)
our_sum(98, 65)    


#keyword variable arguments

def display(fixed, **kwargs):
    print("the fixed argument is", fixed)
    for x, y in kwargs.items():
        print("key is {} and value is {}".format(x,y))


display(5 , rollno = "00023")
display(5 , rollno = "00025", name = "Agniswar")


#passing group of elements to a function
print("Ente numbers separating with a space")
list = [int(x) for x in input().split()]
suml = sum(list)
print(suml)

# Recursive function
def factorial(n):
    if n== 0:
        result =1
    else:
        result = n*factorial(n-1)
    return result

for i in range(0,11):
    print("factorial if {} is {} ".format(i, factorial(i)), end="\n")


# use of lambda function
f = lambda x:x*x
print(f(5))

f2 = lambda x,y:x+y
print(f2(5,6))

list1 =  [2,6,5,836,99,54,55,89,123,4456,789]
def is_even(x):
    if x%2==0:
        return True
    else:
        return False

list2 = list(filter(is_even, list1))
print(list2)   


#decorator functions

def decor(fun):
    def inner():
        value = fun()
        return value +9
    return inner


def number():
    return 65


result = decor(number)
print(result())



def decor(fun):
    def inner():
        value = fun()
        return value +9
    return inner

@decor
def number():
    return 65


print(number())
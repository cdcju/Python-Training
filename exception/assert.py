try:
    x = int(input("Enter a number"))
    assert x >=25 and x<50
    print("the number is {}".format(x))
except AssertionError:
    print("The condition is not fulfilled")    
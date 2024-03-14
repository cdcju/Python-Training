import logging
logging.basicConfig(filename="log.txt", level=logging.NOTSET)

try:
    a = int(input("Enter a number"))
    b = int(input("enter another number"))
    c=a/b
except Exception as e:
    logging.exception(e)
else:
    print("the result is {}".format(c))


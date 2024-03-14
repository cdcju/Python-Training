a = int(input("Enter first number"))
b = int(input("Enter second number"))

print("value of a nd b before {} and {}".format(a,b))

# a,b = b,a

# print("value of a nd b after {} and {}".format(a,b))

if b==3 and b%2 == 0:
    print("it is even")
elif b==0:
    print("it is zero")
else:
   print("it is odd")  


while a>5:
    print("while loop")
    a = a-1

for i in range(1,16,2):
    print(i)


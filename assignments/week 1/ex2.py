floatNumbers = []
n = int(input("Enter the list size : "))


for i in range(0, n):
    print("Enter {}th number".format(i), ":")
    item = float(input())
    floatNumbers.append(item)
    
print("User List is ", floatNumbers)
avg = sum(floatNumbers)/n
print("The average of {} numbers is {:0.2f}".format(n, avg)) #:0.2f rounds floting point number upto two digits
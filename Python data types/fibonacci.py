n = int(input("Enter the max limit"))
i=1
a=0
b=1
i=0
# print("{} {}".format(a, b), end ='\t')
while b<n:
    print("{}".format(b), end ='\t')
    t=a+b
    a=b
    b=t
    i=i+1

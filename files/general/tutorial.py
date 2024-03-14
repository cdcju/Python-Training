#creating a file  and store some character

f = open("mytext.txt", 'w')
strn  = input("Enter a string")
f.write(strn)
f.close()


#read from a file
f = open("mytext.txt", 'r')
strn = f.read()
print(strn)
f.close()

#aapend a string to a file
f = open("mytext.txt", 'a+')
print("Enter a string, put @ at the end")
str = ""
while str!='@':
    str = input()
    if(str!= '@'):
        f.write(str+"\n")

# f.seek(offset, fromwhere, put the pointer at the begining of the file
f.seek(0,0)

str2 = f.read()
print(str2)

#closing the file
f.close()


#check a file exist or not

import os
import  sys

fname = input("Enter the file name")
if os.path.isfile(fname): #checking the filename with its directory
    f = open(fname, 'r')
else:
    print("There is no such file")
    sys.exit()  



str = f.read()
print(str)
f.close()



# open a file with 'with' statement

with open("mytext2.txt", 'w') as f:
    f.write("HELLO CDC")
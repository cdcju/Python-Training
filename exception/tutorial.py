# Exception handling

# try:
#     statement
# except ex1 :
#     statement
# except ex2:
#     statement
# else:
#     statement
# finally:
#     statemant            

try:
    name= input("Enter an file name")
    f = open(name, 'r')
except IOError:
    print("File name doesnot exist")
else:
    n = len(f.readline())   
    print(name, "has" , n , "lines" )      


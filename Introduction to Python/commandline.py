#taking parameter from commandline argument
import sys

arg = sys.argv
length = len(arg)

print(" The number of arguments is {}".format(length))
for i in arg:
    print(i)
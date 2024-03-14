#while loop

word =['Apple', 'Mango', 'Grape', 'five', 'Six']
n=0
while(n<5):
    print(word[n])
    n+=1


#python for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#for loop in strings

for x in "banana":
  print(x)


#With the break statement we can stop the loop before it has looped through all the items and the continue statement we can stop the current iteration of the loop, and continue with the next

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


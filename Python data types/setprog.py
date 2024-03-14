#simply create a set

myset = {"apple", "banana", "cherry"}
print(myset) #print the set
 #same value will be ignored
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print(len(thisset)) # getting the legth of the set

set1 = {"abc", 34, True, 40, "male"} #various types of elements
print(set1)

thisset2 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset2)

# for loop
for x in thisset:
       print(x)

thisset = {"apple", "banana", "cherry"}

# retrun true or false if it is in the set
print("banana2" in thisset)      

# add elements in the set
thisset.add("orange")

print(thisset)


#update two sets to each echer

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# update a set with a list
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove a element from a set

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#discard can be used for this
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# union operation of two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#intersection of two sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
# symetric difference of two sets and the update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
# symetric difference of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#clear all the elements of a set  i.e become empty
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#copy a set
thisset = {"apple", "banana", "cherry"}

s2 = thisset.copy()

print(s2)


#differnce between two sets and the updated 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) # just use x.difference(y) only get the difference
print(x)

# pop operation 

x = {"apple", "banana", "cherry"}
x.pop() # not suitable operation in set
print(x)
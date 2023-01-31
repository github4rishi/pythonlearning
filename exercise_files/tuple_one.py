#!/usr/bin/python3

# define a tuple
my_empty=()
myTuple=(3,4,5)

print(my_empty)
print(myTuple)

print(bool(my_empty)) # empty tuple bool will be false
print(bool(myTuple)) # True

myNewTuple=(3,4,[5,6,7],8,9)
print(myNewTuple)

print(myNewTuple[0])
print(myNewTuple[2])
print(myNewTuple[2][1])

#myTuple[0]=22 # Tuples are immutable, that means you can modify the value of tuple
#print(myTuple)

myTuple_new=(3,3,4,5,6,7,7,8,10)
print(myTuple_new)

print(myTuple_new[3:])
print(myTuple_new[:])
print(myTuple_new[3:5])

x=3,4,7,9
print(x,type(x))

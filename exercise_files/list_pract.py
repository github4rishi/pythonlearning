#!/usr/bin/python3

myList1=[3,3,4,"python",5.6]
print(myList1[0])
print(myList1[-1]) # print last value 
print(myList1[-2]) # print 2nd list value

print(myList1[3][1]) # value in index 3 and then char 2
print(myList1[:]) # print entire list

print(myList1[0:]) # print from index 0 to last
print(myList1[1:]) # print from index 1 to last

print(myList1)
print(myList1[:])
print(myList1[0:])


# modify index value, that means list are mutable
# string are immutable
myList1[0]=45
print(myList1)

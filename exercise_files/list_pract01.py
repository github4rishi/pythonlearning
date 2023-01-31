#!/usr/bin/python3

myList=[3,5,2,7,3,8,5,5,9]
extend_myList=[9,99]
print(myList.index(5)) # value at index 5

print(myList.count(10)) # value 10 in the defined list
print(myList.count(5)) #  count value 5 in the defined list

print(myList)
myList.append(111)
print(myList)

myList.insert(1,45)
print(myList)

myList.extend(extend_myList)
print(myList)

myList.remove(8)
print(myList)

myList.pop()
print(myList)

myList.pop(0)
print(myList)


print(myList.pop()) # print value that pop() will remove
print(myList)

myList.sort() # arrange in ascending order
print(myList)

myList.reverse()
print(myList)


myList.sort(reverse=True)
print(myList)

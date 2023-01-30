#!/usr/bin/python3
# practice list

myList=[1,2,3,4,5]

print(myList)
myList.clear() # clear the list
print(myList)

myList=[1,5,6,8]
eMyList=[9,8,4,5]
myList.append(10)
print(myList)

myList.insert(1,44)
print(myList)

print(myList.pop())
print(myList)

print("pop value at index 0")
print(myList.pop(0))
print(myList)

myList.extend(eMyList)
print(myList)

myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)



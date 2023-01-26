#!/usr/bin/python3
# append() function to the list
# insert() function to insert value
# extend() to extend the list

my_list=[1,4,7,8]
new_list=[9,10]

my_list.append(56) # append value 56 to the list
print(my_list)

my_list.insert(1,45) # insert value 45 to index 1
print(my_list)

my_list.extend(new_list) # extend list with new list
print(my_list)

my_list.remove(8) # remove value from the list
print(my_list)

my_list.pop() # remove last index value
print(my_list)

print(my_list.pop()) # print the value pop() will remove 
print(my_list) # print list 

print(my_list.pop(0)) # print the value in index 0 that will be removed 
print(my_list)

my_list.sort() # sort the list, ascending order
print(my_list) 

my_list.sort(reverse=True) # sort the list in descending order
print(my_list)



my_list.reverse() # reverse the list
print(my_list)

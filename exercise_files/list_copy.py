#!/usr/bin/python3
# with copy() differnet memory location would be allocated.

my_list=[3,4,5,6,7,8]

my_new_list=my_list.copy()
my_list_nocopy=my_list

print(my_new_list)
print(my_list_nocopy)

# print memory location 
print(id(my_list),id(my_list_nocopy)) # mem loc would be same
print(id(my_new_list)) # mem location would be differnet

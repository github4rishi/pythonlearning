#!/usr/bin/python3

# string are immutable, lower() and upper() functions for lowercase and uppercase

my_string="Python scripting"
print(my_string.lower())
print(my_string.upper())
print(my_string)


# assign to a var
mystrLower=my_string.lower() # lower() function to change to lowercase
mystrUpper=my_string.upper() # upper() function to change to uppercase

print(f"mystr lowercase {mystrLower}") 
print(f"mystr uppwercase {mystrUpper}")

# swapcase upper change to lower and vice versa
print(my_string.swapcase())

# change string to title format, that is each word in starting should be capital
print(my_string.title())

# capitlize() - first char would be changed to uppercase
print(my_string.capitalize())

# casefold() - instead of lower() we can use this funtion as well. 


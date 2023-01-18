#!/usr/bin/python3

mystr=""
my_new_str=" "
print(f'{bool(mystr)}')
print(f'{bool(my_new_str)}')

my_fav_scripting="Python scripting"
print(f'My fav scripting language is {my_fav_scripting}')

# print last char of the string (-1)
print(f'print last char of the string: {my_fav_scripting[-1]}') 

# print first char of the string (0)
print(f'print first char of the string: {my_fav_scripting[0]}')

# print range of chars 
print(f'print chars from 0 to 3: {my_fav_scripting[0:3]}' )

# print length of a string
myStrLen=len(my_fav_scripting)

print(f'Length of a given string is: {myStrLen}')
print(f'Length of a string is: {len(my_fav_scripting)}')




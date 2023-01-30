#!/usr/bin/python3

keys=['a','e','i','o','u']
new_dict=dict.fromkeys(keys)
print(new_dict)
new_dict['a']='first vowel'
print(new_dict)

# set default
my_dict={}

# key is there, okay otherwise set default key
my_dict.setdefault('k',45)
print(my_dict)


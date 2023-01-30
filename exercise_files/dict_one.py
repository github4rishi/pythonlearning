#!/usr/bin/python3
# define dict

my_dict={}
print(my_dict,type(my_dict))

print(bool(my_dict)) # False value as its empty

# dictionary consists of  key-value pairs.

my_dict={'fruit' : 'apple',
	 'animal' : 'fox',
	 '1': 'one',
	 'two': '2'
	}

print(my_dict)

# Access dictionary based on keys.

print(my_dict['fruit'])
print(my_dict.get('animal'))
print(my_dict.get('three'))

print(my_dict)
#my_dict.clear() # clear the dictionary 
#print(my_dict)


my_dict['three']=3 # key value 'three' is absent so it will create a key-value pair
print(my_dict)

my_dict['three']=55 # it will modify now
print(my_dict)


print(my_dict.keys()) # print keys
print(my_dict.values()) # print values
print(my_dict.items()) # print items


y=my_dict.copy() # differnet memory location
print(y)
print(id(y),id(my_dict)) 


newDict={'four':'4'}
my_dict.update(newDict) # update old dict 
print(my_dict)

my_dict.pop('four')
print(my_dict)

removed_item=my_dict.popitem()
print(removed_item)
print(my_dict)




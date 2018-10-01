#!/usr/bin/env python

# Python Dictionaries
#
# Dictionary
#
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and the have keys and values.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print (thisdict)

# Accessing Items
#
# You can access the items of a dictionary by referring to its key name:

x = thisdict["model"]
x = thisdict.get("model")

# Change Values
#
# You can change the value of a specific item by referring to its key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Loop Through a Dictionary
#
# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# Dictionary Length
#
# To determine how many items (key-value pairs) a dictionary have, use the len method.
print( len(thisdict) )

# Adding Items
#
# Adding an item to the dictionary is done by using a new index key and
# assign a value to it:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing Items
#
# There are several methods to remove items from a dictionary:

# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
#print(thisdict) # this will cause an error because "thislist" no longer exists.

# The clear() keyword empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# The dict() Constructor
#
# It is also possible to use the dict() constructor to make a dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)


# Dictionary Methods
#
# Python has a set of built-in methods that you can use on dictionaries.
#
# Method                Description
# clear()               Removes all the elements from the dictionary
# copy()                Returns a copy of the dictionary
# fromkeys()            Returns a dictionary with the specified keys and values
# get()                 Returns the value of the specified key
# items()               Returns a list containing the a tuple for each key value pair
# keys()                Returns a list containing the dictionary's keys
# pop()                 Removes the element with the specified key
# popitem()             Removes the last inserted key-value pair
# setdefault()          Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()              Updates the dictionary with the specified key-value pairs
# values()              Returns a list of all the values in the dictionary

#!/usr/bin/env python

# Python Lists
#
# Python Collections (Arrays)
#
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# List
#
# A list is a collection which is ordered and changeable.
# In Python lists are written with square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access Items
# You access the list items by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# List Length
# To determine how many items a list have, use the len() method:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove Item
# There are several methods to remove items from a list:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)  # this will cause an error because "thislist" no longer exists

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# The list() Constructor
# It is also possible to use the list() constructor to make a list.
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# List Methods
#
# Python has a set of built-in methods that you can use on lists.
#
# Method            Description
# append()          Adds an element at the end of the list
# clear()           Removes all the elements from the list
# copy()            Returns a copy of the list
# count()           Returns the number of elements with the specified value
# extend()          Add the elements of a list (or any iterable), to the end of the current list
# index()           Returns the index of the first element with the specified value
# insert()          Adds an element at the specified position
# pop()             Removes the element at the specified position
# remove()          Removes the item with the specified value
# reverse()         Reverses the order of the list
# sort()            Sorts the list

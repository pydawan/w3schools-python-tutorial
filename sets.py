#!/usr/bin/env python

# Python Sets

# Set
#
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so the items will appear in a random order.

# Access Items
#
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyworkd.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Change Items
#
# Once a set is created, you cannot change its items, but you can add new items.

# Add Items
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# To add more than one item to a set use the update() method.
thisset = {"apple", "banana", "cherry"}
thisset.update(["orage", "mango", "grapes"])
print(thisset)

# Get the Length of a Set
#
# To determine how many items a set have, use the len() method.
thisset = {"apple", "banana", "cherry"}
print( len(thisset) )

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# The set() Constructor
#
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Set Methods
#
# Python has a set of built-in methods that you can use on sets.
#
# Method                            Description
# add()                             Adds an element to the set
# clear()                           Removes all the elements from the set
# copy()                            Returns a copy of the set
# difference()                      Returns a set containing the difference between two or more sets
# difference_update()               Removes the items in this set that are also included in another, specified set
# discard()                         Remove the specified item
# intersection()                    Returns a set, that is the intersection of two other sets
# intersection_update()             Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()                      Returns whether two sets have a intersection or not
# issubset()                        Returns whether another set contains this set or not
# issuperset()                      Returns whether this set contains another set or not
# pop()                             Removes the specified element
# symmetric_difference()            Returns a set with the symmetric differences of two sets
# symmetric_difference_update()     Inserts the symmetric differences from this set and another
# union()                           Return a set containing the union of sets
# update()                          Update the set with the union of this set and others

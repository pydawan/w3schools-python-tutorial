#!/usr/bin/env python

# Python Arrays

# Arrays are used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]

# What is an Array?
#
# An array is a special variable, which can holde more than one value at a time.
# If you have a list of items (a list of car names, for example), storing cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# Access the Elements of an Array
x = cars[0]

# Modify the value of the first array item:
cars[0] = "Toyota"

# The Length of an Array
x = len(cars)
print(x)

# Looping Array Elements
for x in cars:
    print(x)

# Adding Array Elements
cars.append("Honda")

# Removing Array Elements

# Delete the second element of the cars array:
cars.pop(1)

cars.append("Volvo")

# Delete the element that has the value "Volvo":
cars.remove("Volvo")


# Array Methods
#
# Python has a set of built-in methods that you can use on lists/arrays.
#
# Method                                    Description
# append()                                  Adds an element at the end of the list
# clear()                                   Removes all the elements from the list
# copy()                                    Returns a copy of the list
# count()                                   Returns the number of elements with the specified value
# extended()                                Add the elements of a list (or any iterable), to the end of the current list
# index()                                   Return the index of the first element with the specified value
# insert()                                  Adds an element at the specified position
# pop()                                     Removes the element at the specified position
# remove()                                  Removes the first item with the specified value
# reverse()                                 Reverses the order of the list
# sort()                                    Sorts the list

# Note: Python does not have built-in support for Array, but Python Lists can be used instead.


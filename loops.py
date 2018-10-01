#!/usr/bin/env python

# Python For Loops
#
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dctionary, a set, or a string).
# This is less like the for keyword in other programming language, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand.

#Loop Through a String
#
# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
#
# To loop through a set of code a specified number o fimtes, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by addin a parameter:
# range(2, 6), which means values from 2 to 6 (but no including 6):
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x)

# Else in For Loop
#
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
#
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Recursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
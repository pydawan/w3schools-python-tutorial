#!/usr/bin/env python

# Python Strings

# String Literals
#
# String  literals in Python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
#
# Strings can be output to screen using the print function. For example: print("Hello")
#
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

# Substring. Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print( a.strip() ) # returns "Hello, World!"

# The len() method returns the length of a string:
a = "Hello, World!"
print( len(a) )

# The lower() method returns the string in lower case:
a = "Hello, World!"
print( a.lower() )

# The upper() method returns the string in upper case:
a = "Hello, World!"
print( a.upper() )

# replace() method replaces a string with another string:
a = "Hello, World!"
print( a.replace("H", "J") )

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print( a.split(",") ) # returns ['Hello', ' World!']

# Command-line String Input
#
# Python allows for command line input.
# That means we are able to ask the user for input.
# The following example asks for the user's name, then, by using the input() method, the program prints the name to the screen:
#print('Enter your name:')
#x = input()
x = raw_input("Enter your name: ")
print("Hello, " + x)

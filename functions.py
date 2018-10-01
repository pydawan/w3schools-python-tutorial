#!/usr/bin/env python

# Python Functions

def my_function():
    print("Hello from a function")

# Calling a Function
my_function()

# Parameters
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Default Parameter Value
#
# If we call the function without parameter, it uses the default value:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Return Values
#
# To let a function return a value, use the return statement:
def my_function(x):
    return 5 * x

print( my_function(3) )
print( my_function(5) )
print( my_function(9) )
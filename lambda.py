#!/usr/bin/env python

# Python Lambda
#
# A lambda function is a small anonymous function.
# A lambda function can take any number of argument, but can only have one expression.

# Syntax
# lambda arguments : expression

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))


# Lambda functions can take any number of arguments:
x = lambda a, b: a * b
print(x(5, 6))

# A lambda function that sums argument a, b e c and print the result:
x = lambda a, b, c: a + b + c
print( x(5, 6, 2) )

# Why Use Lambda Functions?
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print( mydoubler(11) )
print( mytripler(11) )
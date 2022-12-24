# %%
print("hello world")

# %%
# This a python comment

"""This is multiline comment in python"""

'''This is also
for multiline comment purpose'''

# %%
# how to declare variables in python
myNumber = 3

# multi declaration
a, b, c = "husnul", 23, ['aceh', 'bandung', 'jakarta']

# change type
strb = str(b)

# conditional operator

money = 3 if 30 % 3 == 0 else 0

print("money", money)

intstrb = int(strb)

print(strb)
print(intstrb)

myNumber2 = 4.6

print(myNumber)
print(myNumber2)

myNumber = "Hello This My Number"  # Change to diff data type
print(myNumber)

# %%
# Taking the input

problem = input("tell us your problem")

print(problem)
print(type(problem)) # to check variable type

# Python program showing
# a use of raw_input() in python 2
# g = raw_input("Enter your name : ")
# print g


# we also able to typecasting input
# to specific data type
# by default it typecasted to str (string)
amount = int(input())
amount = float(input())


# %%
# taking multiple inputs

# Using split() method :
boy, girl = input().split()
print(boy)
print(girl)

# %%
# Output using print() function
# print(value(s), sep= ' ', end = '\n', file=file, flush=flush)

a, b, c, d = 1, 2, 3, 4

print(a,b,c,d, sep=" ")
print(a,b,c,d, sep="*")
print(a,b,c,d, sep="*", end="/end/")
print()

# without flush
import time

count_second2 = 3
for i in reversed(range(count_second2 + 1)):
	if i > 0:
		print(i, end='>>>')
		time.sleep(1)
	else:
		print('Start')

# with flush
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i == 3:
		time.sleep(1)
	if i > 0:
		print(i, end='>>>', flush = True)
		time.sleep(1)
	else:
		print('Start')


# %%
# print without new line

# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line

print("geeks", end =" ")
print("geeksforgeeks")

# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in range(4):
	print(a[i], end =" ")

# Print without newline in Python 3.x without using for loop

l=[1,2,3,4,5,6]

# using * symbol prints the list
# elements in a single line
print(*l)

import antigravity # LOL must try

# %%
# Output Formatting

# Python program showing how to use
# string modulo operator(%) to print
# fancier output

# print integer and float value
print("Geeks : %2d, Portal : %0.2f" % (1000, 5.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))

# Python program to
# format a output using
# string() method

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))


# %%
# LIST IN PYTHON , SLICE IN GO

myList = []

print(myList)

myList.append("Hello")
myList.append("Husnul")
myList.append(1)
myList.append(["hello", 1,2,"husnul"])
myList.append(3.4)

print(myList)

# %%
# INPUT FUNCTION
name = input("Please insert your name ")

print("your name is " + name)

# %%
# CONDITIONAL / SELECTION

myNumber = int(input("insert a number"))
if (myNumber == 1):
    print("ONE")
elif(myNumber < 3):
    print("less than 3")
else:
    print("uncommon number")

# %%
# FUNCTION
name = input("...TYPE YOUR NAME...")
def printMyName(name):
    print("Your name is "+ name)

printMyName(name)

def printANumber(num):
    print("You choose number " + num)

printANumber(num=input("...A NUMBER PLEASE ..."))

# %%
# How to run a main function
def getANumber():
    res = int(input("... A number please ..."))
    return res

def Main():
    print("START")

    out = getANumber()
    print(out)

if (__name__ == "__main__"):
    Main()

# %%
# LOOPING 
for i in range (5): # For integer only
    print(i)

# %%
import math

pi = math.pi

def CircleArea(pi, radius):
    area = pi * math.pow(radius,2)
    return area
CircleArea(pi, 4)

# %%
# WHILE LOOP

count = 0

while (count < 5):
    print(count)
    count = count + 1

# %%
# PYTHON KEYWORD
import keyword

print(keyword.kwlist)

# %%
# TRUE AND FALSE
print(False == 0)
print(False == -1)
print(True == 1)
print(True == 2)

print(True+True)
print(False+False)
print(False+True)

print(None == 1)
print(None == 0)
print(None == False)
print(None == [])
print(None == {})

# %%
# AND, OR, NOT, IN, IS

print(True or False)
print(True and False)
# or: This a logical operator in python. “or” Return the first True value.if not found return last. The truth table for “or” is depicted below. 
# and: This a logical operator in python. “and” Return the first false value. If not found return last. The truth table for “and” is depicted below.
print(1 or 3 or 10 or 20)
print(10 or 3 or 1 or 2)
print(1 and 3 and 10 and 20)
print(10 and 3 and 1 and 2)

# not: This logical operator inverts the truth value. The truth table for “not” is depicted below. 
# in: This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.
# is: This keyword is used to test object identity, i.e to check if both the objects take the same memory location or not.

print (not 1 ==1)
print (not 1 !=1)

print("s" in "husnul")
print("s" in "HUSNUL")
print("s" in "HUSNULS")
print("s" in "HUSNULs")

print(" " is " ") # will show warning

print({} is {})

# %%
# FOR, WHILE, BREAK, CONTINUE
for i in range (10):
    print(i, end=" ")

    if (i == 6): break

print()

c = 0
while c < 10:
    if c == 6:
        c += 1
        continue
    else:
        print(c, end=" ")
        c += 1

# %%
# RETURN AND YIELD

# yield is like return but used to return a generator

def firstPrime():
    return 2

print(firstPrime())

def fun():
    S = 0

    for i in range (10):
        S += 2
        yield S

for i in fun():
    print(i)

# %%
# CLASS
class Human:
    Name = "Husnul"
    Age = 23

print(Human.Name)
print(Human.Age)

# %%
# AS

import math as m

print(m.pi)

# %%
n = 10
for i in range(n):
	
# pass can be used as placeholder
# when code is to added later
	pass


# %%
# Lambda keyword is used to make inline returning functions with no statements allowed internally. 

# Lambda keyword
g = lambda x: x*x*x

print(g(7))

# %%
# import keyword
import math
print(math.factorial(6))

# from keyword
from math import factorial
print(factorial(6))

# %%
# Exception Handling Keywords

# try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.
# except : As explained above, this works together with “try” to catch exceptions.
# finally : No matter what is result of the “try” block, block termed “finally” is always executed.
# raise: We can raise an exception explicitly with the raise keyword
# assert: This function is used for debugging purposes. Usually used to check the correctness of code. If a statement is evaluated to be true, nothing happens, but when it is false, “AssertionError” is raised. One can also print a message with the error, separated by a comma.
a = 5
b = 0

try:
    print(a//b)
except:
    print("unable to divide by zero")
finally:
    print("always executed")

assert b != 0, "divisor can not be zero" #error thrower



# %%
# del keyword
# del is used to delete a reference to an object. Any variable or list value can be deleted using del.

my_variable1 = 20
my_variable2 = "Hello"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# delete both the variables
del my_variable1
del my_variable2

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)


# %%
# global and non local
# global: This keyword is used to define a variable inside the function to be of a global scope.
# non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.
n1 = 15
def add():
    n2 = 2
    global n1
    n1 = n1 + n2
    print(n1)

print(n1)
add()

# %%
# Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

# Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 8 + 9)

# Declared using square brackets [] :
footballer = ['MESSI',
          'NEYMAR',
          'SUAREZ']

# Declared using braces {} :
x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}

# Declared using semicolons(;) :
flag = 2; ropes = 3; pole = 4

print(s)
print(n)
print(x)
print(flag, " ", ropes, " ", pole)

# %%
# operators in python
# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b

# Subtraction of numbers
sub = a - b

# Multiplication of number
mul = a * b

# Division(float) of number
div1 = a / b

# Division(floor) of number
div2 = a // b

# Modulo of both number
mod = a % b

# Power
p = a ** b

# print results
print("add ",add)
print("sub ",sub)
print("mul ",mul)
print("div1 ",div1)
print("div2 ",div2)
print("mod ",mod)
print("power ",p)


# %%
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

# a is not b is True
print(a is not b)

# a is b is False
print(a is b)


# %%
# logical operator
# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)


# %%
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


# %%
# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)


# %%
# identity operator
a = 10
b = 20
c = a

print(a is not b)
print(a is c)


# %%
# Python program to illustrate
# not 'in' operator
# or membership operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")


# %%
# Examples of Operator Precedence

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
	print("Hello! Welcome.") # this will be executed
else:
	print("Good Bye!!")


# %%
# Examples of Operator Associativity

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)


# %%
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)


# %%
# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print
print({True: a, False: b} [a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())


# %%
# Python program to demonstrate nested ternary operator
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a")

# Python program to demonstrate nested ternary operator
a, b = 10, 20

if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")

a=5
b=7

# [statement_on_True] if [condition] else [statement_on_false]

print(a,"is greater") if (a>b) else print(b,"is Greater")

'''When condition becomes true, expression [on_false]
   is not executed and value of "True and [on_true]"
   is returned.  Else value of "False or [on_false]"
   is returned.
   Note that "True and x" is equal to x. 
   And "False or x" is equal to x. '''

	
# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)




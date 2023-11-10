##############################################
## This is a Python cheat sheet
## This cheat sheet is based on the following tutorial:
## https://www.youtube.com/watch?v=rfscVS0vtbw
##############################################

import math

##############################################
## Getting Started
##############################################

# Use # to comment out your code

# this is how you print to the console
print("Hello World")

# how to declare a variable
x = 5 # x is an integer
y = 5.5 # y is a float
name = "John" # name is a string
is_whatever = True # is_whatever is a boolean

# how to print a variable
print(x)

# how to print a string and a variable
print("My name is " + name)
print("My name is", name)
print("My name is %s" % name)
# concatenate multiple strings using %
print("Hello %s %s" % ("World", name))


##############################################
## String Manipulation
##############################################

# strings in new lines
print("Hello\nWorld")

# Escape characters
print("Hello \"World\"")

# lowercase
print("Hello World".lower()) # this will print "hello world"
print("Hello World".islower()) # this will print "False"

# uppercase
print("Hello World".upper()) # this will print "HELLO WORLD"
print("Hello World".isupper()) # this will print "False"
print("Hello World".upper().isupper()) # this will print "True"

# length
print(len("Hello World")) # this will print "11"

# get first character
print("Hello World"[0]) # this will print "H"

# get last character
print("Hello World"[-1]) # this will print "d"

# get characters from index 1 to 4
print("Hello World"[1:4]) # this will print "ell"

# get characters from index 1 to the end
print("Hello World"[1:]) # this will print "ello World"

# get characters from the beginning to index 4
print("Hello World"[:4]) # this will print "Hell"

# get characters from the beginning to the end
print("Hello World"[:]) # this will print "Hello World"

# get index of a character
print("Hello World".index("W")) # this will print "6"

# replace a character
print("Hello World".replace("H", "J")) # this will print "Jello World"


##############################################
## Numbers
##############################################

# how to print a number
print(5)

# sum
print(5 + 5) # this will print "10"

# subtract
print(5 - 5) # this will print "0"

# multiply
print(5 * 5) # this will print "25"

# divide
print(5 / 5) # this will print "1.0"

# modulo
print(5 % 5) # this will print "0"

# math expressions
print(5 * 5 + 5) # this will print "30"
print(5 * (5 + 5)) # this will print "50"

# how to convert a number to a string
print(str(5))

# how to convert a number to a float
print(float(5))

# how to convert a number to an integer
print(int(5.5))

# how to check if a number is an integer
print(type(5)) # this will print "<class 'int'>"

# how to check if a number is a float
print(type(5.5)) # this will print "<class 'float'>"

# how to check if a number is a string
print(type("5")) # this will print "<class 'str'>"

# absolute value
print(abs(-5)) # this will print "5"

# power
print(pow(2, 3)) # this will print "8"

# max
print(max(4, 6)) # this will print "6"

# min
print(min(4, 6)) # this will print "4"

# round
print(round(3.2)) # this will print "3"

# floor
print(math.floor(3.7)) # this will print "3"

# ceil
print(math.ceil(3.7)) # this will print "4"

# square root
print(math.sqrt(36)) # this will print "6.0"


##############################################
## Input
##############################################

name = input("Enter your name: ")
print("Hello %s!" % name)


##############################################
## Lists
##############################################

# A list is a collection of items in a particular order

# how to declare a list
countries = ["USA", "Canada", "Mexico", "Brazil", "Peru", "Chile"]

# print all items in a list
print(countries)

# print the first item in a list
print(countries[0])

# print the last item in a list
print(countries[-1])

# print the first 3 items in a list
print(countries[0:3])

# print the last 3 items in a list
print(countries[-3:])

# print the length of a list
print(len(countries))

# add an item to the end of a list
countries.append("Argentina")

# add an item to a specific index
countries.insert(1, "Colombia")

# remove an item from a list
countries.remove("Brazil")

# remove the last item from a list
countries.pop()

# remove an item from a specific index
countries.pop(1)

# clear a list
countries.clear()

# copy a list
countries = ["USA", "Canada", "Mexico", "Brazil", "Peru", "Chile"]
countries_copy = countries.copy()

# count the number of times an item appears in a list
print(countries.count("USA"))

# sort a list
countries.sort()

# reverse a list
countries.reverse()

# join a list
countries = ["USA", "Canada", "Mexico", "Brazil", "Peru", "Chile"]
countries_string = ", ".join(countries)
print(countries_string)

# convert a string to a list
countries = countries_string.split(", ")
print(countries)

# merge two lists
countries = ["USA", "Canada", "Mexico", "Brazil", "Peru", "Chile"]
countries2 = ["Argentina", "Colombia"]
countries.extend(countries2)
print(countries)

# count the number of items in a list
print(len(countries))

# counf the number of times an item appears in a list
print(countries.count("USA"))

# list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)

# 2D list
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbers[0][0]) # this will print "1"
print(numbers[1][1]) # this will print "5"
print(numbers[2][2]) # this will print "9"

##############################################
## Tuple
##############################################

# A Tuple is a collection of items in a particular order that cannot be changed
# Tuples are immutable
# The difference between a list and a tuple is that a list uses square brackets and a tuple uses parenthesis

# how to declare a tuple
countries = ("USA", "Canada", "Mexico", "Brazil", "Peru", "Chile")

# print all items in a tuple
print(countries)

# print the first item in a tuple
print(countries[0])

# print the last item in a tuple
print(countries[-1])

# print the first 3 items in a tuple
print(countries[0:3])

# print the last 3 items in a tuple
print(countries[-3:])

# print the length of a tuple
print(len(countries))

# count the number of times an item appears in a tuple
print(countries.count("USA"))

# convert a tuple to a list
countries = list(countries)
print(countries)

# convert a list to a tuple
countries = tuple(countries)
print(countries)


##############################################
## Dictionary
##############################################

# Dictionary is a collection of key-value pairs

# how to declare a dictionary
countries = {
    "USA": "Washington DC",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasilia",
    "Peru": "Lima",
    "Chile": "Santiago"
}

# print all items in a dictionary
print(countries)

# print the value of a key
print(countries["USA"])
print(countries.get("USA"))
print(countries.get("Bolivia", "Not Found")) # if the key does not exist, return "Not Found"

# add a key-value pair to a dictionary
countries["Argentina"] = "Buenos Aires"

# remove a key-value pair from a dictionary
del countries["Brazil"]

# remove all key-value pairs from a dictionary
countries.clear()

# count the number of key-value pairs in a dictionary
print(len(countries))

# get all keys in a dictionary
print(countries.keys())

# get all values in a dictionary
print(countries.values())

# get all key-value pairs in a dictionary
print(countries.items())

# copy a dictionary
countries = {
    "USA": "Washington DC",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasilia",
    "Peru": "Lima",
    "Chile": "Santiago"
}
countries_copy = countries.copy()

# merge two dictionaries
countries = {
    "USA": "Washington DC",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasilia",
    "Peru": "Lima",
    "Chile": "Santiago"
}
countries2 = {
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota"
}
countries.update(countries2)
print(countries)


##############################################
## Conditionals
##############################################

# how to declare an if statement
if 5 > 2:
    print("5 is greater than 2")
    
# how to declare an if statement with an else statement
if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")
    
# how to declare an if statement with an elif statement
if 5 > 2:
    print("5 is greater than 2")
elif 5 == 2:
    print("5 is equal to 2")
else:
    print("5 is not greater than 2 and 5 is not equal to 2")
    
# how to declare an if statement using an AND operator
if 5 > 2 and 5 > 3:
    print("5 is greater than 2 and 5 is greater than 3")

# how to declare an if statement using an OR operator
if 5 > 2 or 5 > 3:
    print("5 is greater than 2 or 5 is greater than 3")

# how to declare an if statement using a NOT operator
if not 5 > 2:
    print("5 is not greater than 2")

# how to declare an if statement using a common test and a NOT operator
if 5 > 1 and not 5 > 2:
    print("5 is not greater than 2")

# compare equal strings
if "Hello" == "Hello":
    print("Hello is equal to Hello")

# compare unequal strings
if "Hello" != "World":
    print("Hello is not equal to World")


##############################################
## Looping
##############################################

# how to declare a while loop
i = 1
while i < 6:
    print(i)
    i += 1
    
# how to declare a while loop with a break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
# how to declare a while loop with a continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
# how to declare a for loop
for i in range(6):
    print(i)

# how to declare a for loop with a break statement
for i in range(6):
    print(i)
    if i == 3:
        break

# how to declare a for loop with a continue statement
for i in range(6):
    if i == 3:
        continue
    print(i)
    
# how to declare a for loop with a range
for i in range(2, 6):
    print(i)

# how to declare a for loop with a range and a step
for i in range(2, 6, 2):
    print(i)

# how to declare a for loop with a range and a negative step
for i in range(6, 2, -1):
    print(i)

# how to declare a for loop with a list
countries = ["USA", "Canada", "Mexico", "Brazil", "Peru", "Chile"]
for country in countries:
    print(country)
    
# how to declare a for loop with a string
for letter in "Hello World":
    print(letter)

# looping a 2D list
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in numbers:
    for column in row:
        print(column)


##############################################
## Try Except
##############################################

# how to declare a try except statement
try:
    print(x)
except:
    print("An exception occurred")
    
# how to declare a try except statement with an else statement
try:
    print("Hello World")
except:
    print("An exception occurred")
else:
    print("No exception occurred")
    
# how to declare a try except statement with a finally statement
try:
    print(x)
except:
    print("An exception occurred")
finally:
    print("The 'try except' is finished")
    
# handling specific exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    
# handling multiple exceptions
try:
    print(x)
except (NameError, TypeError):
    print("Variable x is not defined or the data type is incorrect")
except:
    print("Something else went wrong")
    
# how to capture the exception message
try:
    print(x)
except Exception as e:
    print(e)
    
# how to declare a try except statement with a raise statement
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# how to declare a try except statement with a raise statement and a custom exception
x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

##############################################
## Functions
##############################################

# how to declare a function
def myFunction():
    print("Hello World")
    
# how to call a function
myFunction()

# how to declare a function with parameters
def myFunction(name):
    print("Hello %s" % name)
    
# how to call a function with parameters
myFunction("John")

# how to declare a function with a default parameter
def myFunction(name = "John"):
    print("Hello %s" % name)
    
# how to call a function with a default parameter
myFunction()

# how to declare a function with a return value
def myFunction(name):
    return "Hello %s" % name

# how to call a function with a return value
print(myFunction("John"))

# how to declare a function with multiple parameters
def myFunction(name, age):
    print("Hello %s, you are %s years old" % (name, age))
    
# how to call a function with multiple parameters
myFunction("John", 20)

# how to declare a function with multiple parameters and default values
def myFunction(name = "John", age = 20):
    print("Hello %s, you are %s years old" % (name, age))
    
# how to call a function with multiple parameters and default values
myFunction()

# how to declare a function with an arbitrary number of arguments
def myFunction(*kids):
    print("The youngest child is " + kids[2])
    
# how to call a function with an arbitrary number of arguments
myFunction("John", "Bob", "Mike")

# how to declare a function with an arbitrary number of keyword arguments
def myFunction(**kid):
    print("His last name is " + kid["lname"])

# how to call a function with an arbitrary number of keyword arguments
myFunction(fname = "John", lname = "Doe")

# how to declare a function with a default parameter and an arbitrary number of arguments
def myFunction(name = "John", *kids):
    print("The youngest child is " + kids[2])

# how to call a function with a default parameter and an arbitrary number of arguments
myFunction("John", "Bob", "Mike")

# how to declare a function with a default parameter and an arbitrary number of keyword arguments
def myFunction(name = "John", **kid):
    print("His last name is " + kid["lname"])
    
# how to call a function with a default parameter and an arbitrary number of keyword arguments
myFunction(fname = "John", lname = "Doe")

# how to declare a function with a default parameter, an arbitrary number of arguments, and an arbitrary number of keyword arguments
def myFunction(name = "John", *kids, **kid):
    print("The youngest child is " + kids[2])
    print("His last name is " + kid["lname"])
    
# how to call a function with a default parameter, an arbitrary number of arguments, and an arbitrary number of keyword arguments
myFunction("John", "Bob", "Mike", fname = "John", lname = "Doe")


##############################################
## Classes and Objects
##############################################
    
# how to declare a class
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def printName(self):
        print("My name is " + self.name)

# how to create an object
myObject = MyClass("John")

# how to call a method
myObject.printName()

# how to modify an attribute
myObject.name = "Bob"
myObject.printName()

# how to delete an attribute
del myObject.name
myObject.printName()

# how to delete an object
del myObject
myObject.printName() # this will throw an error because myObject no longer exists

# how to declare a class that inherits from another class
class MyChildClass(MyClass):
    pass

# how to create an object from a child class
myChildObject = MyChildClass("John")

# how to call a method from a child class
myChildObject.printName()

# how to declare a class that inherits from another class and has a second method
class MyChildClass(MyClass):
    def printAnother(self):
        print("Another output for " + self.name)
        
myChildObject = MyChildClass("John")
myChildObject.printName()
myChildObject.printAnother()

# how to override a method from a parent class
class MyChildClass(MyClass):
    def printName(self):
        print("My name is " + self.name + " and I am a child")
        
myChildObject = MyChildClass("John")
myChildObject.printName()

# how to call a method from a parent class
class MyChildClass(MyClass):
    def printName(self):
        print("My name is " + self.name + " and I am a child")
        
    def printParentName(self):
        super().printName()

myChildObject = MyChildClass("John")
myChildObject.printName()
myChildObject.printParentName()

# how to declare a class with a private attribute
class MyClass:
    def __init__(self, name):
        self.__name = name
        
    def printName(self):
        print("My name is " + self.__name)
        
myObject = MyClass("John")
myObject.printName()
print(myObject.__name) # this will throw an error because __name is a private attribute

# how to declare a class with a private method
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def __printName(self):
        print("My name is " + self.name)
        
myObject = MyClass("John")
myObject.__printName() # this will throw an error because __printName is a private method

# how to declare a class with a private attribute and a getter method
class MyClass:
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
        
    def printName(self):
        print("My name is " + self.__name)
        
myObject = MyClass("John")
myObject.printName()
print(myObject.getName())

# how to declare a class with a private attribute and a setter method
class MyClass:
    def __init__(self, name):
        self.__name = name
        
    def setName(self, name):
        self.__name = name
        
    def printName(self):
        print("My name is " + self.__name)
        
myObject = MyClass("John")
myObject.printName()
myObject.setName("Bob")
myObject.printName()

# how to declare a class with a private attribute and a getter method and a setter method
class MyClass:
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name
        
    def printName(self):
        print("My name is " + self.__name)
        
myObject = MyClass("John")
myObject.printName()
myObject.setName("Bob")
myObject.printName()
print(myObject.getName())

# how to declare a class with a private attribute and a getter method and a setter method and a deleter method
class MyClass:
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name
        
    def printName(self):
        print("My name is " + self.__name)
        
    def delName(self):
        del self.__name
        
myObject = MyClass("John")
myObject.printName()
myObject.setName("Bob")
myObject.printName()
print(myObject.getName())
del myObject.name # this will throw an error because __name is a private attribute


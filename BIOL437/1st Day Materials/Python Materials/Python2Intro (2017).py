
# coding: utf-8

# In[ ]:

#! /usr/bin/env python

# Welcome to the python primer! 
# This was written in 2017 by Ammon Perkes for use in Junhyong Kim's Comp Bio class
# It is based in large part on slides made by Sarah Middleton
# For questions contact perkes.ammon@gmail.com


# In[ ]:

print("Hello, world!")


# In[ ]:

# Notice that you can write comments using the hash sign (aka pound, number, sharp, octothorpe). 
# Commenting is never necessary for your code to run
# But well commented code will make it much easier to read, including for yourself
# You can also comment out a single line of code: 
# print "Hello, world!"

"""
You can also use strings to comment out entire sections quickly
this is especially useful for debugging 
print helloworld
the convention here is to use three double quotes
like so
Notice if you're running this in the interpreter you'll get some output
"""


# In[ ]:

print("Today we will be going over a few topics")
print("1. Creating a Python Script")
print("2. Variables and data types")
print("3. if-else statements")
print("4. Loops")
print("5. Lists")
print("6. Application: String-Matching Algorithm")


# In[2]:

#1. Creating a python script
# Try the following lines of code:
print("Hello " + ",world!")
print("Hello", "world")
print(1,2,3)
print(123)
print(1+1)
print(2*3)
print("1+1")
print("1" + "1")


# In[ ]:

#2. Variables

# x is a variable
x = 7 
print x


# In[ ]:

# There are rules to naming variables
goodName = "This is a well named variable"
good_name = "So is this"
goodNAME = "This is fine, but note that it's different from goodName"
bskjd = "this is a badly named variable"


# In[ ]:

print(goodName)


# In[ ]:

7eleven = "this is an illegal variable"
print = "so is this"
two names = "No spaces"
na%ed = "Any of these will break your code"


# In[ ]:

# There are several types of Variables, we'll generally talk about 4
myStr = "This is called a string"
myInt = 7 # This is an int, for integer. It holds a counting number (-2,-1,0,1,2 etc)
myFloat = 7.0 # This is a float, it has a decimal, and is handled differently than integers
myBool = True # This is a bool, for boolean variable. It's used in logical operations, discussed below


# In[ ]:

# Variables are determined at declaration
var1 = "This is a string"
print(var1)


# In[ ]:

# We can change var1, so that it becomes an int
var1 = 2 
print(var1 + 2)


# In[ ]:

# Variables behave differently depending on their type. Think about what the following lines of code will do:
myGene = "Fmr1"
print(geneID)


# In[ ]:

apples = 5
oranges = 10
fruit = apples + oranges
print(fruit)


# In[ ]:

print(apples + oranges)


# In[ ]:

print(apples, oranges)


# In[ ]:

print("I have", apples, "apples")


# In[ ]:

# How do variables change? 
people = 3
print(people + 1)
print(people)


# In[ ]:

people = 3
people = people + 1
print(people)


# In[ ]:

people = 3
animals = 4
people = animals
print(people)
print(animals)


# In[ ]:

myAge = 28
print("You will be", (yourAge + 1), "next year")


# In[ ]:

yourAge = "16"
print("You will be", (yourAge + 1), "next year")


# In[ ]:

#fyi, you can still do this by using a conversion function
yourAge = "16"
print("You will be", int(yourAge) + 1, "next year")


# In[ ]:

## 3. Logical Statements: if-else


# In[5]:

daytime = False

print( "Go west on Guardian Dr")
print( "Turn right on University Ave")
if daytime:
    print( "Continue straight on University for 3 blocks")
else:
    print( "After crosswalk, cut across on the pedestrian path")
    print( "Continue diagonally past the Love Statue, the button, and walnut")
print( "Turn right on Chestnut")
print( "Continue through JFK")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

# How to use if-else statments
if conditional:
    'this code is executed'
else:
    'this other code is executed'

# Remember that your conditional must already be defined


# In[ ]:

# Logic practice: 

a = False
if a:
    print( "this statement is true")


# In[7]:

# Other Examples: 
# if a and b are True
# if a or b is True
# if a is True but b is not
# if a greater than b and b is positive
a = True 
b = False
a and not b

# What do these conditionals mean:

# if a != b and b >= c:
# if (a != b or b == 7) or (a >= 7 and b == "apple"):


# In[ ]:

# You can also do this with comparisons
x = 5
if x > 0:
    print( "x is positive")
else:
    print( "x is negative ")


# In[ ]:

if x >= 0:
    print( "x is a whole number")


# In[ ]:

a = 4 
b = 7
c = 6


# In[ ]:

if c > a and c < b:
    print( "c is between a and c")


# In[ ]:

if c != a:
    print( "c is not a")
else:
    print( "c is a!")


# In[ ]:

# Obviously, we're not limited to numerical comparisons: 
myLetter = "a"
letterOfDay = "a"
if myLetter == letterOfDay:
    print myLetter + " is the letter of the day!"


# In[ ]:

# You can also nest conditionals
if x > 0:
    print( "x is positive")
else:
    if x == 0:
        print( "x is zero")
    else:
        print( "x is negative")


# In[ ]:

## For and While Loops

print( "for:")
for n in range(5):
    print( n)
    

print( "while:")
n = 0
while n < 5:
    print( n)
    n = n + 1
 


# In[8]:

# For Loops:
# An easy way to make a for loop is using the range function
for n in range(5):
    print( "Hello!")


# In[9]:

# What does range actually do? 

range(5)


# In[13]:

# You can also make for loops with strings
for i in "MY STRING":
    print( i)

# Note that you don't need to define the variable (in this case the letter) in advnace


# In[14]:

# What will this print?
for i in range(4):
    print( i)


# In[ ]:

# While loops
# While loops repeat until some condition is met
count = 0
while count < 5:
    print( "Hello" )
    count = count + 1

# (Not just a complicated 'for' loop)


# In[16]:

# Wait for user input
correctAnswer = 10
yourAnswer = 0

while yourAnswer != 10:
    yourAnswer = input("What is the square root of 100? ")
    yourAnswer = int(yourAnswer)




# In[ ]:

# Count number of steps
# How many steps to get to 1,000,000? 


# In[ ]:

# Non-exhaustive searches


# In[ ]:

# Watch out for endless loops! 


# In[17]:

# Lists! 
myList = ["cat",2,"Ammon",False,204]
print( myList)


# In[24]:

myList[:3]


# In[ ]:

# You can access and change elements in a list:
# Note the index starts with 0
print( myList[0])


# In[25]:

# You can use range to automatically make lists of numbers:
myNums = list(range(5,50,5))
print( myNums)


# In[26]:

# You can't access outside of the lists size: 
print( myList)


# In[27]:

# If you want to add to a list, use the append function
myList.append("one more!")
print( myList)

# Note that we didn't need to say myList = myList.append('x')


# In[28]:

# To remove an object from a list, use the pop function
myList.pop(2)
print( myList)


# In[29]:

myList.append([1,2,3])
print( myList)


# In[31]:

fakeArray = [[1,2,3],[4,5,6],[7,8,9]]
print( fakeArray)


# In[32]:

fakeArray[1][1]


# In[ ]:

# Searching within a list" 

'cat' in myList


# In[ ]:

# Strings often act like lists
myString = "HELLO I AM A STRING"
myString[3]


# In[ ]:

for letter in myString:
    print( letter)


# In[ ]:

# You can also use len(myString)
# But strings *aren't* lists, for reasons that you can google


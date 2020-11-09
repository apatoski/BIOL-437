
# coding: utf-8

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[18]:


# Try the following lines of code:
print("Hello " + ",world!")
print("Hello", "world")
print(1,2,3)
print(123)
print(1+1)
print(2*3)
print("1+1")
print("1" + "1")


# In[25]:

print("1"+"apple")


# In[28]:

# Introduce variables
print = 'now it is a string'


# In[31]:

# Variables Behave differently depending on their type. 
# Think about what the following lines will do: 
apples = 5
oranges = 10
fruit = apples + oranges
print(fruit)


# In[32]:

bananas = 'bananas'
grape_fruit = 'grapefruit'
my_fruits = bananas + grape_fruit
print(my_fruits)


# In[35]:

#print(fruit)
#print(apples + oranges)
#print(apples + 10)
#print("I have", apples, "apples")
print("I have " + str(apples) + " apples")


# In[40]:

myString = "27"
print(int(myString) + 20)
print("I can't type this")
print('This is a "quote"')


# In[3]:

# When do variables change and when don't they? 
x = 7
y = x
y = 8
print(x + y)


# In[41]:

# Reminder, variables behave differently depending on their type ("5" + 1)


# In[51]:

# Boolean Variables
myBool = True
print(myBool)

print(myBool + 1)


# In[48]:

7 >= 5


# In[6]:

# 3. If Else statements


# In[52]:

# Logic Practice
a = False
b = True


# In[54]:

if b:
    print('Answer 1')
    print('If it is true')
print('print this regardless')


# In[55]:

if a:
    print ('Answer 1')
else:
    print ('Answer 2')


# In[58]:

b = True
if a:
    print('Answer 1')
elif b:
    print('Answer 2')
else:
    print('Answer 3')


# In[59]:

a and b


# In[60]:

a or b


# In[61]:

b and not a


# In[62]:

a != b


# In[63]:

c = 7
(a != b and b >= c)


# In[16]:

# Non numberical comparisons (strings)


# In[64]:

# Nesting Conditionals


# In[67]:

for i in range(5):
    print('hello')
    print(i)


# In[70]:

range(5)


# In[ ]:




#! /usr/bin/env python
import re

## Read the two strings into memory
query_file = open('query.txt','r')
query_string = query_file.readline()
query_file.close()
database_file = open('database.txt','r')
database_string = database_file.readline() ## Note this only works because we can read the whole database into memory

database_file.close()

search_string = ''
search_string2 = ''

# Use modular arithmetic to build a search string with characters and wild cards for regex
# This isn't a general solution, but it works for this case
p1 = 10
d1 = 14

## initially I just went for the length of the string
## But that actually caused me to miss one hit at the tail end of the database.
for i in range((p1 - 1) * (d1 + 1) + 1):
    if i % 15 == 0:
        search_string = search_string + query_string[i]
    else:
        search_string = search_string + '.'

p2 = 10
d2 = 13
for i in range((p2 - 1) * (d2 + 1) + 1):
    if i % 14 == 0:
        search_string2 = search_string2 + query_string[i]
    else:
        search_string2 = search_string2 + '.'

print('first 18 characters: ',query_string[:18])
print('gapped p-mer search string (p=10,d=14):',search_string)
print('gapped p-mer search string (p=10,d= 13):',search_string2)


# Find using 18mer
## I don't know why regex syntax is so counterintuitive, but here it is: 
a = [m.start() for m in re.finditer(query_string[:18],database_string)]
print('locations for simple 18-mer:',a)

# Find using gapped p-mer (d = 14)
b = [m.start() for m in re.finditer(search_string,database_string)]
print('locations for gapped p-mer:',b)


# Find using gapped p-mer (d = 13)
c = [m.start() for m in re.finditer(search_string2,database_string)]
print('locations for gapped p-mer:',c)

#! /usr/bin/env python

## Code for Question 6 of Homework 3
## Made 9/28/18. Contact Ammon Perkes (aperkes@sas.upenn.edu) for questions
## I know it's going to bother some people that I didn't use if __name__ == "__main__"
## But I started hacking it together and then never stopped. 

## File name of string to be built
string_fname = 'q6_string.txt'
query_fname = 'q6_query.txt'

global alphabet, alpha_dict
alphabet = ['A','C','G','T']
alpha_dict = dict(zip(alphabet,range(len(alphabet))))

## Read in and (gently) sanitize input
string_file = open(string_fname)
database_string = string_file.readline()
database_string = database_string.strip().upper()
string_file.close()

query_file = open(query_fname)
query_string = query_file.readline()
query_string = query_string.strip().upper()
query_file.close()

## Hard coded tables, if you want to go that route: 
"""
perm_table = ['$CGAACAT', 
              'AACAT$CG', 
              'ACAT$CGA', 
              'AT$CGAAC', 
              'CGAACAT$', 
              'CAT$CGAA', 
              'GAACAT$C', 
              'T$CGAACA']

BWT = 'TGAC$ACA'
suffix_array = [7,2,3,5,0,4,1,6]
B_table =  [[0, 0, 1, 1, 2, 2, 2, 3], 
            [0, 0, 0, 1, 1, 1, 2, 2], 
            [0, 1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1, 1]]
N_table = [0, 3, 5, 6, 7]
"""

## Quick function to avoid having to call global everytime i need to convert letter to number
def letter_to_number(letter):
    global alpha_dict
    return alpha_dict[letter]

## Index all the letters in the string. I use this a lot for the sorting
def index_letters(data_string):
## This is a different alphabet from the main alphabet...I should have build this better...
    alphabet = ['$','A','C','G','T'] # Initially, i didn't add '$' and it made lots of things hard 
    index_dict = dict(zip(alphabet,[[] for n in alphabet]))
    for i in range(len(data_string)):
        index_dict[data_string[i]].append(i)
    return index_dict

# Little function to count the number of letters (handy for ordering, N_table)
def count_letters(data_string):
    alphabet = ['$','A','C','G','T']
    count_dict = dict(zip(alphabet,[0 for a in alphabet]))
    for i in database_string:
        try:
            count_dict[i] += 1
        except:
            print('Something in your string is broken')
            sys.exit()
    return count_dict

## Significantly more complicated (but functional) function to get sorted string, bwt, and suffix array
## I just wanted to alphabetize a string, but this is where I get everything
## Makes permutation table, builds BWT, gets suffix array
def alphabetize(data_string):
    if data_string[-1] != '$':
        data_string = data_string + '$'
    index_dict = index_letters(data_string)
    perm_table = ['' for n in data_string]
    sorted_string = ''
    BWT = ''
    for p in range(len(perm_table)):
        permutation = data_string[p:] + data_string[:p]
        perm_table[p] = permutation
    ## Need a function to sort permutation while keeping track of indices. at that point i might as well just get everything
    sorted_indices = sort_string(data_string)
    # From sorted indices, it's easy to build both the alphabetized string and the BWT
    # Interestingly, it turns out you don't even need the permutation table, it's encoded in the methodology below
    for s in sorted_indices:
        sorted_string += data_string[s]
        BWT += data_string[s-1]
    return BWT,sorted_indices, sorted_string

## This is a fun little recursive alphabetization function. 
# It would have been a lot esier to use a pre-packaged sort function. But think of the learning!
# By the way, the string here can be thought of as the first column. 
# When it hits ambiguity (A vs. A) it looks in the next column, given with the modular operator (%) on line 115 below
def sort_string(single_string):
    index_dict = index_letters(single_string)
    print('searching:',single_string,' using: ',index_dict)
    sorted_indices = []
    for k in index_dict.keys():
        #print(k)
        #print(index_dict[k],len(index_dict[k]))
        if len(index_dict[k]) == 0: # if there's none, that's easy
            pass
        elif len(index_dict[k]) == 1: # if there's one, add its index
            sorted_indices.append(index_dict[k][0])
        else: # If there's ambiguity, you have to look to the next letters
            next_column = [n + 1 for n in index_dict[k]] 
            next_indices = []
            next_string = ''
            for i in next_column:
                next_string += single_string[i%len(single_string)]
                next_indices.append(i)
                ## If the next string is all the same letters, move forward by one more
            while check_variety(next_string) == False:
                print('Your string was broken, so I will fix it.')
                new_string = ''
                for n in range(len(next_string)):
                    new_string += single_string[next_indices[n] + 1]
                next_string = new_string
            print('go deeper...:',next_string)
            sorted_next = sort_string(next_string)
            print('sorted_next:', sorted_next)
            for s in sorted_next:
                #print(s,k)
                sorted_indices.append(index_dict[k][s])
    return sorted_indices

def check_variety(next_string):
    for n in range(len(next_string)):
        if next_string[n] != next_string[0]:
            return True
        else:
            continue
    return False

# Function to build B_table
def build_Btable(BWT,alphabet):
    # build a quick conversion table, seed table (I could do this with numpy, but I wanted to keep it simple)
    B_table = [[0 for n in range(len(BWT))] for m in range(len(alphabet))]
    for i in range(len(BWT)):
        if BWT[i] == '$': ## A bit hackish, sorry, but otherwise it breaks when it reads '$'
            l_index = len(alphabet) + 1
        else:
            # Get next index value and add 1 to it
            l_index = letter_to_number(BWT[i])
            B_table[l_index][i] = B_table[l_index][i-1] + 1
            #print(B_table)
        for l in range(len(alphabet)):
            if l != l_index:
                # Fill in next column from rows
                #print(l,i,l_index)
                B_table[l][i] = B_table[l][i - 1]
    #print(BWT,B_table)
    return B_table

# Builds N table as list not dict, which will require a bit of transforming, but allows for mathematical operations
def build_Ntable(count_dict, alphabet):
    N_table = [0 for n in range(len(alphabet)+1)]
    #print(N_table,alphabet,count_dict)
    for n in range(1,len(alphabet)+1):
        N_table[n] = N_table[n-1] + count_dict[alphabet[n-1]]
    #print(N_table)
    return N_table

# recursive functions to get everything
# These are straight out of the reading
def bwt_min(xW_string,N_table,B_table):
    if len(xW_string) == 1:
        return N_table[letter_to_number(xW_string)] + 1
    else:
        x = xW_string[0]
        x_index = letter_to_number(x)
        W = xW_string[1:]
        min_xW = N_table[x_index] + B_table[x_index][bwt_min(W,N_table,B_table) - 1] + 1
        return min_xW

def bwt_max(xW_string,N_table,B_table):
    if len(xW_string) == 1:
        return N_table[letter_to_number(xW_string) + 1]
    else:
        x = xW_string[0]
        x_index = letter_to_number(x)
        W = xW_string[1:]
        max_xW = N_table[x_index] + B_table[x_index][bwt_max(W,N_table,B_table)]
        return max_xW


#database_string = "ATACTA"
#query_string = "TAAT"
   
## Build BWT...figure out how to do it on paper (see picture)
# Comment out these lines if you want to use the hard coded tables
count_dict = count_letters(database_string)
#BWT, suffix_array, sorted_array = build_bwt(database_string)
BWT, suffix_array, sorted_string = alphabetize(database_string)
B_table = build_Btable(BWT, alphabet)
N_table = build_Ntable(count_dict, alphabet)

#query_string = 'AA'
print('BWT:',BWT)
print('Suffix Array:',suffix_array)
print('Sorted String:',sorted_string)
print('N_table:',N_table)
print('B_table:\n',B_table)
print('Database String:',database_string)
print('Search String:',query_string)
min_row = bwt_min(query_string,N_table,B_table)
max_row = bwt_max(query_string,N_table,B_table)

print('Min/Max:',min_row,max_row)

if min_row == max_row:
    print('String found at Offset:',suffix_array[min_row])
elif min_row < max_row:
    print('String found at offsets:',suffix_array[min_row:max_row + 1])
elif min_row > max_row:
    print('String not found.')



## fin ##

#### Bad functions that are rather instructive: 

## Function to create the borrows-wheeler transform of a string
## Also returns suffix_array and sorted string (pulled from alphabetize above)
# This actually works, as long as you sort the string correctly and have the suffix array
def build_bwt(data_string):
    sorted_string, suffix_array = alphabetize_poorly(data_string)
    sorted_string = '$' + sorted_string
    data_string = data_string + '$'
    perm_table = [''] * 8 ## It's going to be a lot easier to have each sub list be a row
    BWT = ''
    for s in range(len(suffix_array)):

        suf_index = suffix_array[s]
        permuted_string = ''
        for i in range(len(data_string)):
            next_letter = data_string[(suf_index + i)%len(data_string)]
            permuted_string += next_letter
        perm_table[s] = permuted_string
        ## We can simultaneously compile the BWT, which is actually all we need
        BWT += next_letter
    print(perm_table)
    #print(perm_table,BWT)
    ## Might as well return everything so I only have to do these functions once
    return BWT, suffix_array, sorted_string


# Surprisingly complicated (and broken) function to alphabetize string while returning suffix array
# Incidentally, this is where my biggest error happened
def alphabetize_poorly(data_string):
    indices = list(range(len(data_string)))
    count_dict = count_letters(data_string)
    sorted_string = ''
    sorted_indices = [7] ## since I'm not doing anything with $ yet
    for k in count_dict.keys():
        # This will add the number of letters, in order (because our keys were added alphabetically)
        sorted_string += k * count_dict[k]
        ## I need a little loop that will build the suffix array, because we're not allowed to use sort :/
        #add the indices to a list, this doesn't work! it will break everything
        for i in range(len(data_string)):
            if data_string[i] == k:
                sorted_indices.append(i)
        
    return sorted_string, sorted_indices



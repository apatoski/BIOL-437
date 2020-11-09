
# coding: utf-8

# # Question1

# In[1]:


# A)
Prob_ATACAG = 0.3*0.4*0.9*0.3*0.5*0.4
print("Prob_ATACAG =",Prob_ATACAG)
Hiest_Prob = 0.7*0.4*0.9*0.4*0.5*0.4 #just choose the base with highest probability for each position.
print("Hiest_Prob =",Hiest_Prob)


# In[2]:


def motif_detector(string):
# profile
    profile = [[0.3,0.0,0.0,0.7],
            [0.0,0.4,0.4,0.2],
            [0.9,0.0,0.0,0.1],
            [0.0,0.3,0.3,0.4],
            [0.5,0.1,0.1,0.3],
            [0.2,0.2,0.2,0.4]]       
# print(profile[0][3])

    for i in range (0,len(string)-6):
        substring = string[i+1:i+7]
        prob = 1
        for j in range (0,len(substring)):
            if substring[j] == "A":
                prob = prob * profile[j][0]
            elif substring[j] == "T":
                prob = prob * profile[j][1]
            elif substring[j] == "C":
                prob = prob * profile[j][2]
            elif substring[j] == "G":
                prob = prob * profile[j][3]
        if prob > 0.005:
            print ("The index is", i,"and the probality is", prob)  # or i+1 

# B)
# import fasta file
motif ="""
CCCGTCCGAGAGGAGTACACAGCCGGTGGCCTAGAAACCTCCGCGCCGCGAATCAATACATTTTGAATTCGATTGAAGCTTTCAATACTGAAAGTTAATCTAGTGAATAAATCAAAGAAAATGTGATGCCGTTGAGCAGGAAGTTTACTTCGAAAGGCCACACAAATGTTTTATGTGAAAATTTCTGGATTTGGGATTAAAGTTTTTTATTTAAATTTTAATCAAAACCTTGCGAGTTAGCTCGAAAAAAAGGAGAAGCATTGGCGAATGGATAATATGCACCTGCTCAGGCTGAAGGGAATCAGTGTGTACACGACTCGTAGAGAAAGAGACAACAACCAACTAGTAATCAATCAATTTGACCACATTATTAAATCATCAGGCGTGTCATCGGAGACAAAAATGTGACGAAGAAACATTTGAATCTATGACTTTGAGGATATCAAGTGAGGCGTGAGGATGAGAAGAAGGAAAAGAAAAAATGAAAGCCGGATTTAGGGGAATTGAAAATGAACCGGAAATTGGAAGAATCAAGAGCAGCGGCGAGGAAAAATCAATTTTAGAGAATTTAACATTTTTTTGTGAAATGCAAAACCTGTTTTTTTTTTCTTTTTGAAATTCTGCTAAATTTCAGTTTTAACAAAAAAAACTGATATTTCACTATTTCTGGCCGAAAATCTGCAAAATTCCTCAATTTTCACCTCTAAAAGTAGGGTTCAAGTCAAAAATTGCATTTTTCACATGATTTATGTTGATAAATCGGAAATTTTCAGCTTATTCGTGTTGTTGAAAATCAACTAACTTTGAGTTTTTTGTTTCAATATCGACAAATCGTGTTCTAAATGATTCCTGTGAATTCGGGTACAAATTTGAGAAATTTAAAACATAATTTGGCAAAAAATTTACGAAAAATACAGGAATTTTCAATGGAAATTAAAGGCAGAGAAATAGTCGAAAATTTTGCAGAAAAACCAAAAAAAAATTGGCAAATAAAAGCAACTGTTGCACCTGTTTCCCACGTTTTTCTCCCTATCGCTTCAGAAAACATCTGTCTCCATATGTTTGCATAAGCGTGAAGATTTCGAACGGAAGAACGTCGATTCAAGGACACTTTCTCAGTAAAACGGATTTGAAAGTGATGCCTTGATGACACAGTTTTTAAAATCCACACACCTACGGCTAATTGGGCAAAGTCGATAATTGGAGCAGCAGAGTAAAATCTATAGAAAAATAGAGTGGTGGGAAAGATGGTGTGGGTGAATGGTGGACAAGAAAGTGTACGAATGTGCCTGATGACAAACAGACCCAAGCAGAGGGTGAATGAATGACCAGGGGAAAGGTGCCCCGTGTGAGAAACGGTCCGATGAGATAGTATGCTGAACGAGAGATACACAGACAGTGTGACGCAATGTATGGACTCCTTTTGCACCATTCGTTCGCCACAGTGACCAGAGAAACCCAGTGGAGGAATGAATGAGGGGTGGTAAATTCGAAAATGAATTGAATTCAACTGGAGGGACGGGACACACGATTTGAATTGTATCGAATTAACCCAGAGAAAGACTCTGTGCATAATGAGAAGAGAGGAAGAAGATGGAAAATAGAATCAGTAATTGGAATGCAAGTGAGTGAATGAAAGAGGATTGTAAAAATGAGACTAATTAAATAGGTGGCGGAAATGTCATCTTCTCAGTAATAGTAATAGTTGTAAACTTTGGTGTTTAGGGTTATGCTAATAAAATTCTGATTTACGAAGCTATTTATTATGGGTGTATTTGAATTATTTTCTACTACGAAAAAAACTGCAAAATAATTACTAGTGAATTTCTGATCTTTTTGCTCGTGAAAAACTTTAAAACTGTTCTTTAACAAATAAATTATGATTTTTATCTTTTTTAAAGCAAAAAACTGGTATTTTTGCATAACAGAGCATCGATTTTAACACTCTCATTGATAATTTAAATAAATAGTGAGTGATTTTTTGAAAAACAAGCGATATTTTCGGAATTTAACTGAAATTTCATGAAAATCAAAAAAATGAAAAGTGTTGGCGCATGTTGGGTTATCGAGAAATGCGCTAGATATCGAAAAGTGCGTCAGTGAAGCAATTTGGAGGCAATTCAAAATTCTTTAGTTGCTTTCTTTGGAAATCATTTTTAATGCTCAAAGCATGAATGTATACTTCATTTAAAACTATATTCAAATTTAAAATAAGTAGACGACCTCTTGACCAACTGTA
"""
print("the length of motif is", len(motif))
motif_detector(motif)


# # Question2

# In[3]:


def MarkProcess(string):
    # initial table and transition table
    starting_table = [0.4,0.1,0.1,0.4]
    trans_table = [[0.0,0.4,0.4,0.2],
                [0.8,0.05,0.05,0.1],
                [0.6,0.1,0.2,0.1],
                [0.1,0.3,0.3,0.3]]
    prob = 1
    num = {"A":0, "T":1 ,"C":2 ,"G":3}
    for i in range(0,6):
        if i == 0:
            prob = prob * starting_table[num[string[0]]]
        if i != 0:
            num[string[i-1]]
            num[string[i]]
            prob = prob * trans_table[num[string[i-1]]][num[string[i]]]
    print(prob)

MarkProcess("ACCTGC")
MarkProcess("AGGTCG")


# In[4]:


# simple hash table example used above
num = {"A":0, "T":1 ,"C":2 ,"G":3}
print(num)
num["T"]


# # Question3

# In[33]:


# Question3
string = "AGTGGAATTAAACATAATTAAAGACTTTAAATATAAGTTTGAATTAAA"
# load profile and transition table
profile = [[0.3,0.0,0.0,0.7],
        [0.0,0.4,0.4,0.2],
        [0.9,0.0,0.0,0.1],
        [0.0,0.3,0.3,0.4],
        [0.5,0.1,0.1,0.3],
        [0.2,0.2,0.2,0.4]]
starting_BG = 0.4
starting_M = 0.6
trans_table = [[0.8,0.2],
               [0.3,0.7]]
prob = 1
num = {"A":0, "T":1 ,"C":2 ,"G":3}
prob_BG = [None] * 8
print(prob_BG)
prob_M = [None] * 8
print(prob_M)

for i in range (0,len(string),6):
    print (i+1)
    substring = string[i:i+6]
    print (substring)
    prob_M_sub = 1 # each 6-mers' M state probability
    p = 6 # 6-mers
    if i == 0:
        prob_BG[i] = starting_BG * (0.25**6)
        print("prob_BG is", prob_BG)
        for j in range(0,p):
            prob_M_sub = prob_M_sub * profile[j][num[substring[j]]]
            prob_M[i] = starting_M * prob_M_sub
        print("prob_M_sub is", prob_M_sub)
        print("prob_M is", prob_M)
    if i != 0:
        for j in range(0,p):
            prob_M_sub = prob_M_sub * profile[j][num[substring[j]]]
        print("prob_M_sub is", prob_M_sub)
        i = int(i/6)
        prob_BG[i] = prob_BG[i-1] * 0.7 * (0.25**6) + prob_M[i-1] * 0.2 * (0.25**6)
        prob_M[i] = prob_BG[i-1] * 0.3 * prob_M_sub + prob_M[i-1] * 0.8 * prob_M_sub
        print("prob_BG is", prob_BG)
        print("prob_M is", prob_M)
        
prob = prob_BG[i] + prob_M[i]
print(0)
print("The probability is", prob)    


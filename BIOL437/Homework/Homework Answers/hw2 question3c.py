# If we really want to build a large FSA for these two motifs, the question could be very complicated, actually 
# you will need at least 24 states.
# Here we try to build a FSA that could detect (C/T)CAGC(T/A)G  (2-infinity) nt  (A/T)GATA(A/G) first, and then we 
# only choose the GATA motifs that its distance to accpeting state for TAL1 is less than 17. 
# You can see that actually FSA is not always convenient, it only needs the the inforamtion of the motif, but 
# the extra information from string or alignment could be very helpful sometimes. 

seq ="""
TTCACCGATTTTTTGCTATTTTCTTCATTTCTCAGCCGATTTTAGTCTTTTTTTTTGTCTAAATTATCAAATTTAACCTT
AAAAATCTGCTAAACCATCTGATTCTTCGCTCACAGAACGATTTTCCCGTCATTTTCCAGTTTTTCCCAATTTCCGCCCG
TAAAATTCCATTTATCCAATTCAAATTACGCCGAATTTGTTGCAATAGTCTTGGCACGGTGCCAATTGGATCTTTTCACG
TCATTTTTGACCATTTTCAAGGTCTTTTCAATGCACTTTTAGGCTGCCTTTGTGAAAAAATAACGGATATTCGAAGTTTT
TCGTGAAAAAAAGTGGAAAATCTAGGAAAAAATCGAGAAAAATAAGGTTTTTAAAAGATTTCAACAGACAAAACCACAAA
ATTTGCTCAAAAAAGCAATTAAAACCAGCAGTTATGATAGATTGAAAAAATTACTTGAAAATATCGATTTTAAGCGATTT
TGTTTTAAAAATACACACAATTTTTAGCGAAATCACACAAAAAATCGAGAAAATCCCAAAAATTTCGTTAAAAACCAACA
AAATTAATGTGAAAATTGGTTTTTTCGCTTTAAAATTGATAAAAATTGATAAAAATTTATTTAAAAAATCACACTTCGGT
CAATCTCTGGGCCATTTGCAGCAATTTAGCAATAAAAATAACGAATTTTCTGATGTTTTAGGCAGAATTTTGGAGATTTT
TAGGGAAAATCTCAAAAAATAACCAAAAATCGCTTTAAAATTGATGAAAATTCCCATTTTCGCCAATTTCTGAACCATTT
TTCCGCAATTTTGACCAGTAAATTGCAAAAAATATCGAAAAATTTTGGATTTTATAATCCAAAATTCTAAAATTTCAAGT
AAAATTCAGCAAAATTTGGTGAAAAAAAATACAAAAAATTACAAAAAATTGGCTCAAAAATCAAATTTTTGCGAAAAAAA
TCGAATTTTAGCCCAATTTTCTTCGATTTCTTCCAAATTTTCACTCATTTTTCGCTTTTTTTCGCTCTTTCAATCAGAAA
TACCCCCTTAAAAATAAATATTTTCCAAAAAGTACACCGACAAACGATGAGCAAACAATCTGTGCCACGTGGGAATTGGT
TTTTTTGTGTTTATTTTACAAAAAATGTCAATTTTTTGCTCAATTTTTCAATTAAAAATCGTAATAATTTGCTATTTTAT
AGTTTAAATTATTGATTTTTAGGTTTTTTTGGCGGGAAAAAAATAAATTTGAAAAAAAAAACGGCGGCGGATGGGGTACA
ACAACAACAACTCAAAGATCAAAAAACGAAACGCGAAAACATTTGAATTGACCCTTCGTTCTTTTTTCTATGTTTTTTTG
CCATTAAAATTGAGTTTTTCGACGTTAAAATGCCGAAAATTCGATAAAAAACTGAAAAAATTGAGTTTTTTCCGGAATTT
TAACCCCAAAAACCGAAAAAAAAATCCCGGAAAATCCCCCAGATTTCACTAAAATCTCCAGTTTTACCAACTTTTTTTTG
TTAATTTAGGTACATTTTGTGGCCAAAATCAAAAAAAAAATGGTAAATAAACTACCAAAATGTGAAAAATTGGATATTAA
TTAAATATAAATTGAATTCTGGACAAAATTGAAATTTTCAATTGATTGAACCATTTTTCTATGTTTTTTTGCCATTAAAA
ATGAGTTTTTGGCGGT
"""
seq = seq.replace('\n','')  #return the string with the \n stripped

#########################################################
#    C/T    C     A     G     C      A     G     any   any     A/T    G      A      T      A      A/G
# q0 --> q1 -> q2 -> q3 -> q4 -> q5 --> q6 -> q7 --> q8 --> q9 -> q10 -> q11 -> q12 -> q13 -> q14 -> q15
#                                    T
#                                   -> q16  # for TC or AC 

# the transition table is hardcoded.

transition_table = {(0, 'A'): 0,    (0, 'T'): 1,    (0, 'C'): 1,     (0, 'G'): 0, 
                    (1, 'A'): 0,    (1, 'T'): 1,    (1, 'C'): 2,     (1, 'G'): 0,
                    (2, 'A'): 3,    (2, 'T'): 1,    (2, 'C'): 2,     (2, 'G'): 0,
                    (3, 'A'): 0,    (3, 'T'): 1,    (3, 'C'): 1,     (3, 'G'): 4,
                    (4, 'A'): 0,    (4, 'T'): 1,    (4, 'C'): 5,     (4, 'G'): 0,
                    (5, 'A'): 6,    (5, 'T'): 16,   (5, 'C'): 2,     (5, 'G'): 0,
                    (6, 'A'): 0,    (6, 'T'): 1,    (6, 'C'): 1,     (6, 'G'): 7,
                    (7, 'A'): 8,    (7, 'T'): 8,    (7, 'C'): 8,     (7, 'G'): 8,
                    (8, 'A'): 9,    (8, 'T'): 9,    (8, 'C'): 9,     (8, 'G'): 9,
                    (9, 'A'): 10,   (9, 'T'): 10,   (9, 'C'): 9,     (9, 'G'): 9,
                    (10, 'A'): 10,   (10, 'T'): 10,   (10, 'C'): 9,    (10, 'G'): 11,
                    (11, 'A'): 12,   (11, 'T'): 10,   (11, 'C'): 9,    (11, 'G'): 9,
                    (12, 'A'): 10,    (12, 'T'): 13,  (12, 'C'): 9,    (12, 'G'): 11,
                    (13, 'A'): 14,    (13, 'T'): 10,  (13, 'C'): 9,    (13, 'G'): 9,
                    (14, 'A'): 15,    (14, 'T'): 10,  (14, 'C'): 9,    (14, 'G'): 15,
                    (15, 'A'): 10,    (15, 'T'): 10,  (15, 'C'): 9,    (15, 'G'): 9,
                    (16, 'A'): 0,    (16, 'T'): 1,  (16, 'C'): 9,    (16, 'G'): 7,
                    }

def multiple_fsm(seq):
    m = len(seq)
    # seq = seq.split()
    print("the lenght of sequence is",m)
    found = False
    
    q_state_num = 0
    # go through the seq from right to left
    i = 0
    TAL_end = 0; GATA_end = 0
    for i in range(m):
        letter = seq[i]
        q_state_num = transition_table[(q_state_num, letter)]
        if q_state_num == 7:# accepting state for TAL1
            TAL_end = i
        if q_state_num == 15:    # accepting state
            GATA_end = i
            print ("found one GATA motif at", i+1)
            if GATA_end - TAL_end < 17:
                print ("found one eligible GATA motif at", i+1)   
                found = True
        i += 1
        
    if found == False:
        print ("Not found")

multiple_fsm(seq)


################################################################
# the result should be:
the lenght of sequence is 1696
found one GATA motif at 440
found one eligible GATA motif at 440
found one GATA motif at 602
found one GATA motif at 612

##################################################################
# If you want to try the complete FSA, Here are some useful codes for your reference.
# Transition table should still be hardcoded.

current_states = [0] * n_states # the vaule should be 0 or 1

for letter in my_string:
    future_states = [0] * n_states
    for s in range(len(states)):
        if states[s] == 1:
            new_states = get_transition[s,letter]
            for new_s in new_states:
                future_states[new_s] = 1
    current_states = list(future_states) # this copies the second list, instead of pointing to future states
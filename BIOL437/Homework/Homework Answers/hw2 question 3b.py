# Here we only consider the case that overlapping motif is not allowed.
seq = "ATTTGATTTTTAGATAACACTAAAA"    # based on 3A, or you could try any other string

# the transition table is hardcoded.
transition_table = {(0, 'A'): 1,    (0, 'T'): 1,    (0, 'C'): 0, (0, 'G'): 0, 
                    (1, 'A'): 1,    (1, 'T'): 1,    (1, 'C'): 0, (1, 'G'): 2,
                    (2, 'A'): 3,    (2, 'T'): 1,    (2, 'C'): 0, (2, 'G'): 0,
                    (3, 'A'): 1,    (3, 'T'): 4,    (3, 'C'): 0, (3, 'G'): 2,
                    (4, 'A'): 5,    (4, 'T'): 1,    (4, 'C'): 0, (4, 'G'): 2,
                    (5, 'A'): 6,    (5, 'T'): 1,    (5, 'C'): 0, (5, 'G'): 6,
                    (6, 'A'): 1,    (6, 'T'): 1,    (6, 'C'): 0, (6, 'G'): 0,
                    }

def fsm(seq):
    m = len(seq)
    # seq = seq.split()
    print("the lenght of sequence is",m)
    found = False
    
    q_state_num = 0
    # go through the seq from right to left
    i = 0
    for i in range(m):
        letter = seq[i]
        print((q_state_num, letter))
        q_state_num = transition_table[(q_state_num, letter)]
        if q_state_num == 6:    # accepting state
            print ("found one GATA motif at", i+1)   
            found = True
        i += 1
        
    if found == False:
        print ("Not found")

fsm(seq)

#######################################################################################

The result will be: 
the lenght of sequence is 25
(0, 'A')
(1, 'T')
(1, 'T')
(1, 'T')
(1, 'G')
(2, 'A')
(3, 'T')
(4, 'T')
(1, 'T')
(1, 'T')
(1, 'T')
(1, 'A')
(1, 'G')
(2, 'A')
(3, 'T')
(4, 'A')
(5, 'A')
found one GATA motif at 17
(6, 'C')
(0, 'A')
(1, 'C')
(0, 'T')
(1, 'A')
(1, 'A')
(1, 'A')
(1, 'A')
##Q1: Calculation##
e_mat = {("V", "A"): 0.25, ("V", "C"): 0.25, ("V", "G"): 0.25, 
         ("V", "T"): 0.25, ("R", "A"): 0.91, ("R", "C"): 0.03,
         ("R", "G"): 0.03, ("R", "T"): 0.03}
t_mat = {("V", "V"): 0.75, ("V", "R"): 0.25, ("R", "V"): 0.10, 
        ("R", "R"): 0.90}

#calculates probability that the given string could be produced by the given sequence of states
def calc_state_string_prob(stateseq, string):
    stateprob = 1
    eprob = 1
    pos = 0
    for state in stateseq:
        eprob *= e_mat[(state, string[pos])]
        state2 = state
        if pos == 0:
            stateprob = 0.5
        else:
            stateprob *= t_mat[(state1, state2)]
        state1 = state
        pos += 1
    return stateprob*eprob

#calculates probability that the 3rd hidden state was "R" given "ATAAA" was produced
def ATAAA_p3R():
    string = "ATAAA"
    stateseqs = ([""], [], [], [], [], [])
    for i in range(1, 6):
        for seq in stateseqs[i-1]:
            seqV = seq + "V"
            seqR = seq + "R"
            stateseqs[i].append(seqV)
            stateseqs[i].append(seqR)
    fiveseqs = stateseqs[5] #generate all sequences with 5 states
    
    ATAAAprob = 0 #probability that ATAAA is produced
    p3R_ATAAA = 0 #probability that ATAAA is produced and 3rd state was "R"
    
    for seq in fiveseqs:
        prob = calc_state_string_prob(seq, string)
        ATAAAprob += prob
        if seq[2] == "R":
            p3R_ATAAA += prob
    print(ATAAAprob) #result was 0.01501
    print(p3R_ATAAA) #result was 0.01315
    
    print(p3R_ATAAA / ATAAAprob)    #result was 0.87668


    
    
    
    


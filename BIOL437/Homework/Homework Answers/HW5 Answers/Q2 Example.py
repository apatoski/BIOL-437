MATRIX = {"A": {"A": 0.73, "C": 0.09, "G": 0.09, "T": 0.09},
          "C": {"A": 0.09, "C": 0.73, "G": 0.09, "T": 0.09},
          "G": {"A": 0.09, "C": 0.09, "G": 0.73, "T": 0.09},
          "T": {"A": 0.09, "C": 0.09, "G": 0.09, "T": 0.73},
          }

S1 = "AGCTA"
S2 = "ACCGA"
totp = 1
for idx, i in enumerate(S1):
    sum = 0
    for x in list(MATRIX):
       sum += 0.25 * (MATRIX[x][S1[idx]] * MATRIX[x][S2[idx]])
    totp *= sum
print(totp)

# answer = 3.68 * 10^-6

from sys import stdin
S = input().rstrip()
#S = "ababc"

SET = set()
L = len(S)
for i in range(1, L+1):
    for j in range(0, L):
        substr = S[j: j+i]
        if len(substr) == i:
            SET.add(substr)
        else:
            break
print(len(SET))

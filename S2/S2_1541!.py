# S2-1541 읽어버린 괄호
from sys import stdin
import re

S = input()
# L = re.split('([-|+|])', S)
S2 = S.split("-")
for idx, sub in enumerate(S2):
    if "+" in sub:
        S3 = sub.split("+")
        val = 0
        for c in S3:
            val += int(c)
        S2[idx] = val
        
result = int(S2[0])
for i in range(1, len(S2)):
    result -= int(S2[i])
print(result)
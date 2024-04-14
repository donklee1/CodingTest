# 9996 S3 
from sys import stdin

def CheckPattern(S, pre_str, post_str):
    if S.startswith(pre_str) == False:
        return False
    S = S.replace(pre_str, "", 1)
    if S.endswith(post_str) == False:
        return False
    return True

N = int(stdin.readline().rstrip())
pattern = stdin.readline().strip()
pre_str, post_str = pattern.split("*")
for _ in range(N):
    S = stdin.readline().strip()
    result = CheckPattern(S, pre_str, post_str)
    if result == True:
        print("DA")
    else:
        print("NE")

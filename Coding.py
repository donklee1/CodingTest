# 20365 s3
from sys import stdin

N = int(stdin.readline().rstrip())
S = list(stdin.readline().rstrip())

def CheckCount(BaseColor, TargetColor):
    count = 0
    for i in range(0, N):
        if (i == 0):
            if (S[0] != BaseColor):
                count += 1
        elif (S[i] == TargetColor) and S[i] != S[i-1]: # 연속된 경우 무시
            count += 1
    return count

C1 = CheckCount("B", "R")
C2 = CheckCount("R", "B")

print(1 + min(C1, C2))

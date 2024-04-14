# Coding.py
#import Library as Lib
# 4134 S4

def IsPrime(N):
    if N < 2:
        return False
    elif N == 2:
        return True
    if N % 2 == 0:
        return False
    LastVal = (int)(N ** (1/2)) + 1
    for denom in range(3,LastVal, 2):
        if N % denom == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    while True:
        if (IsPrime(N) == True):
            print(N)
            break
        N = N + 1

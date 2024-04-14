# Coding.py
#import Library as Lib
# 12789 S3

N = int(input())
#N = 5
SQ = list(map(int, input().split()))
#SQ = list(map(int, "5 4 1 3 2".split()))
STACK = []

Finished = False
order = 1
while (Finished == False):
    #print("order=", order, "SQ=", SQ, "STACK=", STACK)
    if len(SQ) > 0 and SQ[0] == order: # 순번일치
        del SQ[0]
        order += 1
    elif len(STACK) > 0 and STACK[-1] == order:
        del STACK[-1]
        order += 1
    elif len(SQ) > 0:
        v = SQ[0]
        del SQ[0]
        STACK.append(v)
    else:
        break
    if order > N:
        Finished = True
        break

if (Finished == True):
    print("Nice")
else:
    print("Sad")

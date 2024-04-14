# 6603 S2
from sys import stdin

RESULT = []

def DFS(K, start):
    if len(RESULT) == 6:
        for a in RESULT:
            print(a, end=" ")
        print("")
        return
    
    for i in range(start, K):
        RESULT.append(DATA[i])
        DFS(K, i+1)
        RESULT.pop()
            

while True:
    DATA = list(map(int, stdin.readline().split()))
    K = DATA[0]
    DATA.pop(0)
    DATA.sort()
    RESULT = []
    DFS(K, 0)
    print("")
    if K == 0:
        break

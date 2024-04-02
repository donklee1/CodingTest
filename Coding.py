# Coding.py
#import Library as Lib
# 4134 S4

N, M = map(int, input().split())
#N, M = map(int, "4 2".split())

TESTSET = []

def DFS():
    if len(TESTSET) == M: # 정답조건
        for A in TESTSET:
            print(A, end=' ')
        print("")
        return

    for i in range(1, N+1):
        if len(TESTSET) == 0 or i >= TESTSET[-1]:
            TESTSET.append(i)
            DFS()
            TESTSET.pop()

DFS()

            
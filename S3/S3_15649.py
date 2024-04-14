N, M = map(int, input().split())

TESTSET = []

def DFS():
    if len(TESTSET) == M:
        for A in TESTSET:
            print(A, end=' ')
        print("")
        return
    for i in range(1, N+1):
        if (i in TESTSET) == False:
            TESTSET.append(i)
            DFS()
            TESTSET.pop()

DFS()

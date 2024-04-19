# S3_15649 중복없이 M개
N, M = map(int, input().split())

TESTSET = []

def DFS():
    if len(TESTSET) == M:
        print(*TESTSET)
        return
    for i in range(1, N+1):
        if (i in TESTSET) == False: #중복불가
            TESTSET.append(i)
            DFS()
            TESTSET.pop()
DFS()

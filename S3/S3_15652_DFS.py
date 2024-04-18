# S3_15652 중복허용, 비내림
N, M = map(int, input().split())

TESTSET = []
def DFS():
    if len(TESTSET) == M: # 정답조건
        print(*TESTSET)
        return

    for i in range(1, N+1):
        if len(TESTSET) == 0 or i >= TESTSET[-1]: # 비내림
            TESTSET.append(i)
            DFS()
            TESTSET.pop() #백트래킹

DFS()

# 15654 S3

RESULT = []

def DFS(DATA):
    if len(RESULT) == M: # 정답조건
        for A in RESULT:
            print(A, end=' ')
        print("")
        return

    for v in DATA:
        if len(RESULT) == 0 or (v in RESULT) == False:
            RESULT.append(v)
            DFS(DATA)
            RESULT.pop()

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort()
DFS(DATA)

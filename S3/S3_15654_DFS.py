# S3_15654 중복없음, 사전순
RESULT = []

def DFS(DATA):
    if len(RESULT) == M: # 정답조건
        print(*RESULT)
        return

    for v in DATA:
        if len(RESULT) == 0 or (v in RESULT) == False:
            RESULT.append(v)
            DFS(DATA)
            RESULT.pop()

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort() # 사전순, 미리정렬
DFS(DATA)

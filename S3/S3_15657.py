# 15657 S3

N, M = map(int,input().split())
DATA = list(map(int,input().split()))
DATA.sort()
RESULT = [] # 결과항목 출력

def dfs(M):
    if len(RESULT) == M:
        for a in RESULT:
            print(a, end=" ")
        print("")
        return
    
    for i in range(0, N): # 모든경우 루프
        v = DATA[i]
        if len(RESULT) == 0 or RESULT[-1] <= v:
            RESULT.append(v)
            dfs(M)
            RESULT.pop()

dfs(M)

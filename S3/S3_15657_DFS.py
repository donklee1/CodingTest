# S3_15657 사전순, 중복허용

N, M = map(int,input().split())
DATA = list(map(int,input().split()))
DATA.sort()
RESULT = [] # 결과항목 출력

def dfs(M):
    if len(RESULT) == M:
        print(*RESULT)
        return
    
    for v in DATA: # 모든경우 루프
        if len(RESULT) == 0 or RESULT[-1] <= v:
            RESULT.append(v)
            dfs(M)
            RESULT.pop()

dfs(M)

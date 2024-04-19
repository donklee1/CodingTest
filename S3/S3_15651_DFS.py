# S3_15651 중복가능 M개고르기
def DFS():
    if len(L) == M: # 정답조건
        print(*L)
        return
    for i in range(1, N+1): #중복가능하므로 처음부터 루프
        L.append(i)
        DFS()
        L.pop() # Back tracking

N, M = map(int, input().split())
L = []
DFS()


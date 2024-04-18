# S3-15650 : 1~N, M개 오름차순
def DFS():
    if len(L) == M:
        print(*L) # 리스트 공백출력
        return
    for i in range(1, N+1):
        if (len(L) == 0) or i > L[-1]: #오름차순
            L.append(i)
            DFS()
            L.pop() #백트래킹

N, M = map(int, input().split())
L = []
DFS()
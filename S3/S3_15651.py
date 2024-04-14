def DFS():
    if len(L) == M: # 정답조건
        for a in L:
            print(a, end = ' ')
        print("")
        return
    for i in range(1, N+1):
        L.append(i)
        DFS()
        L.pop() # Back tracking

N, M = map(int, input().split())
L = []
DFS()


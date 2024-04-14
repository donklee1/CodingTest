def DFS():
    if len(L) == M:
        for a in L:
            print(a, end = ' ')
        print("")
        return
    for i in range(1, N+1):
        if (len(L) == 0) or i > max(L):
            L.append(i)
            DFS()
            L.pop()

N, M = map(int, input().split())
L = []
DFS()

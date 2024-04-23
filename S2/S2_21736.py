# S2_21736 DFS 친구필요
from sys import stdin
import sys
sys.setrecursionlimit(500000)

N, M = map(int, stdin.readline().split())
Visited = [[False] * M for _ in range(N)]
CAMPUS = []
for i in range(N):
    CAMPUS.append(list(stdin.readline()))

def DFS(y, x):
    global M, N
    global result
    if (x < 0) or (y < 0) or (y >= N) or (x >= M):
        return
    if Visited[y][x] == True:
        return
    Visited[y][x] = True
    if CAMPUS[y][x] == "X":
        return
    if CAMPUS[y][x] == "P":
        result += 1

    DFS(y, x+1)
    DFS(y, x-1)
    DFS(y-1, x)
    DFS(y+1, x)

result = 0
for y in range(N):
    for x in range(M):
        if CAMPUS[y][x] == "I":
            DFS(y, x)
            if result == 0:
                print("TT")
            else:
                print(result)
                break

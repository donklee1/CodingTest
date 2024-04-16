# 16953 S2 정수 A를 B로 바꿈 (가능연산 *2, +1)
from sys import stdin
from collections import deque

A,B = map(int, stdin.readline().split())
min_operator = 10e9
def DFS(A, B, op_count):
    global min_operator
    if A == B:
        min_operator = min(min_operator, op_count)
        return
    if A > B:
        return
    
    DFS(A * 2, B, op_count+1)
    DFS(A*10 + 1, B, op_count+1)

def BFS(A, B):
    q = deque()
    q.append((A, 0)) #tuple
    while len(q) > 0:
        a_val, cnt = q.popleft()
        if a_val == B:
            print(cnt+1) # 1을 더한수 출력
            return
        
        if a_val * 2 <= B:
            q.append((a_val * 2, cnt+1))
        if a_val * 10 + 1 <= B:
            q.append((a_val * 10 + 1, cnt+1))
    print(-1)

BFS(A, B)
#DFS(A, B, 0)
#if (min_operator == 10e9):
#    print(-1)
#else:
#   print(min_operator+1)

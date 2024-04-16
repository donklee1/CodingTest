# 16953 S2 
from sys import stdin

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
    DFS(int(str(A)+"1"), B, op_count+1)

DFS(A, B, 0)
if (min_operator == 10e9):
    print(-1)
else:
    print(min_operator+1)

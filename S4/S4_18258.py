# 18258 S4  deque 사용연습
from sys import stdin
from collections import deque
Q = deque()
N = int(stdin.readline().rstrip())
for _ in range(N):
    cmd = list(stdin.readline().split())
    if cmd[0] == "push":
        Q.append(int(cmd[1]))
    elif  cmd[0] == "pop":
        if len(Q) > 0:
            v = Q.popleft() # pop()->오답
            print(v)
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(Q))
    elif cmd[0] == "empty":
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(Q) > 0:
            print(Q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if len(Q) > 0:
            print(Q[-1])
        else:
            print(-1)

# Coding.py
#import Library as Lib
# 28279 S4
from sys import stdin
from collections import deque
DEQ = deque()
N = int(stdin.readline().rstrip())
for _ in range(N):
    cmd = list(stdin.readline().split())
    if cmd[0] == "1": #앞에 추가
        DEQ.appendleft(int(cmd[1]))
    elif  cmd[0] == "2": #뒤에 추가
        DEQ.append(int(cmd[1]))
    elif cmd[0] == "3": #맨앞출력
        if len(DEQ) > 0:
            v = DEQ.popleft()
            print(v)
        else:
            print(-1)
    elif cmd[0] == "4": # 맨뒤출력
        if len(DEQ) > 0:
            v = DEQ.pop()
            print(v)
        else:
            print(-1)
    elif cmd[0] == "5": # 개수
        print(len(DEQ))
    elif cmd[0] == "6": # 비어있는지
        if len(DEQ) == 0:
            print(1)
        else:
            print(-1)
    elif cmd[0] == "7": #맨앞의 정수
        if len(DEQ) > 0:
            print(DEQ[0])
        else:
            print(-1)
    elif cmd[0] == "8": # 맨뒤의 정수
        if len(DEQ) > 0:
            print(DEQ[-1])
        else:
            print(-1)


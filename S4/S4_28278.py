# S4_28278 스택
import sys
N = int(input())
STACK = []
for _ in range(N):
    CMD = list(map(int, sys.stdin.readline().split())) # --> 시간초과 방지입력 sys.stdin.readline()
    if CMD[0] == 1: # PUSH
        STACK.append(CMD[1])
    elif CMD[0] == 2: # POP
        if len(STACK) > 0:
            print(STACK[-1])
            STACK.pop()
        else:
            print(-1)
    elif CMD[0] == 3: # 스택의 개수
        print(len(STACK))
    elif CMD[0] == 4: # 비어있는지 확인
        if len(STACK) == 0:
            print(1)
        else:
            print(0)
    else:# elif CMD[0] == 5: # 스택값 출력
        if len(STACK) > 0:
            print(STACK[-1])
        else:
            print(-1)

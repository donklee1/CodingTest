# 3986 S4 좋은단어 (A,B로만 이루어짐)
from sys import stdin

N = int(input())
count = 0
# 스택의 구조를 정석으로 풀이
for _ in range(N):
    S = input()
    STACK = []
    for char in S:
        if len(STACK) == 0:
            STACK.append(char)
        else:
            if char == STACK[-1]: # 스택과 동일한 경우 (대칭)
                STACK.pop()
            else:
                STACK.append(char)
    if len(STACK) == 0:
        count += 1

print(count)
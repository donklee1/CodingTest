# Coding.py
#import Library as Lib
# 18258 S4
from sys import stdin
from collections import deque
N = int(input())
Q = deque()
for i in range(1, N+1):
    Q.append(i)

while True:
    if len(Q) == 1:
        v = Q.popleft()
        print(v)
        break
    Q.popleft()
    v = Q.popleft()
    Q.append(v)

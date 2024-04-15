# Coding.py
#import Library as Lib
# S4_2164 deque 자료구조
from sys import stdin
from collections import deque
N = int(input())
Q = deque()
for i in range(1, N+1):
    Q.append(i) # 1..N으로 카드를 구성

while True:
    if len(Q) == 1:
        v = Q.popleft()
        print(v)
        break
    Q.popleft() #가장위의 카드를 버린다
    v = Q.popleft() #가장위의 카드를 
    Q.append(v) #아래로 이동

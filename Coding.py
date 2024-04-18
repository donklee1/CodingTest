# S2-11725
from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
NODE = []
for _ in range(N-1):
    n1, n2 = map(int, stdin.readline().split())
    NODE.append((n1, n2))


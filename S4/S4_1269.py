# S4_1269 : 대창차집합
from sys import stdin
A = set()
B = set()

N, M = map(int, input().split())
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))

AB = A - B
BA = B - A
RESEULT_SET = AB | BA
print(len(RESEULT_SET))

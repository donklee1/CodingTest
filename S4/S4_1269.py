from sys import stdin
A = set()
B = set()

N, M = map(int, input().split())
#N, M = map(int, "3 5".split())
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))
#A = set(map(int, "1 2 4".split()))
#B = set(map(int, "2 3 4 5 6".split()))

AB = A - B
BA = B - A
RESEULT_SET = AB | BA
print(len(RESEULT_SET))

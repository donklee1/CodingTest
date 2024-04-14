# 10816
from sys import stdin

N = int(input())
DATA = list(map(int, input().split()))
M = int(input())
QUERY = list(map(int, input().split()))
#N = 20
#DATA = list(map(int, "6 3 2 10 10 10 -10 -10 7 3".split()))
#M = 8
#QUERY = list(map(int, "10 9 -5 2 3 4 5 -10".split()))

DATA.sort()
dic = {} # dic을 사용하는 방법

for a in DATA:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
for q in QUERY:
    if q in dic:
        print(dic[q], end=" ")
    else:
        print("0", end=" ")

# S4_10816 dict() 사용
from sys import stdin

N = int(input())
DATA = list(map(int, input().split()))
M = int(input())
QUERY = list(map(int, input().split()))

DATA.sort()
dic = {} # dic을 사용하는 방법

for a in DATA:
    if a in dic:
        dic[a] += 1 # 이미존재하므로 기존값 + 1 저장
    else:
        dic[a] = 1
for q in QUERY:
    if q in dic:
        print(dic[q], end=" ")
    else:
        print("0", end=" ")

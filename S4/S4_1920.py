# 1920 이분탐색 S4
from sys import stdin

N = int(input())
DATA = list(map(int, input().split()))
M = int(input())
QUERY = list(map(int, input().split()))
DATA.sort()

def BinSearch(DATA, Q, START, END): # END는 +1값
    if END <= START:
        return 0
    MID = (START + END) // 2
    if DATA[MID] == Q:
        return 1
    elif Q > DATA[MID]:
        return BinSearch(DATA, Q, MID+1, END)
    else: # <
        return BinSearch(DATA, Q, START, MID)

for a in QUERY:
    ret = BinSearch(DATA, a, 0, len(DATA))
    print(ret)

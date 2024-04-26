# S5-1652 누울자리
from collections import deque

N = int(input())
ROOM = []
for _ in range(N):
    ROOM.append(list(input()))

def HorzCount():
    _count = 0
    for i in range(N):
        continue_cnt = 0
        for j in range(N):
            if ROOM[i][j] == '.':
                continue_cnt += 1
            else:
                if continue_cnt > 1:
                    _count += 1
                continue_cnt = 0
        if continue_cnt > 1: # 루프끝에서 다시한번
            _count += 1
    return _count    

def VertCount():
    _count = 0
    for i in range(N):
        continue_cnt = 0
        for j in range(N):
            if ROOM[j][i] == '.':
                continue_cnt += 1
            else:
                if continue_cnt > 1:
                    _count += 1
                continue_cnt = 0
        if continue_cnt > 1: # 루프끝에서 다시한번
            _count += 1
    return _count    

print(HorzCount(), VertCount())
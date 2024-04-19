# S2_15666 M개, 같은수 가능, 비내림

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort() # 비내림

LIST = []
def DFS():
    global N, M
    if len(LIST) == M:
        print(*LIST)
        return
    prev_val = 0
    for i in range(N):
        if DATA[i] != prev_val:
            if len(LIST) > 0 and DATA[i] < LIST[-1]:
                continue
            LIST.append(DATA[i])
            prev_val = DATA[i]
            DFS()
            LIST.pop()

DFS()

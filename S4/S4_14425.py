N, M = map(int, input().split())       
SET_N = {""}
SET_N.remove("") # 좋은방법 아님 (문자열 타입때문)
for _ in range(N):
    A = input()
    SET_N.add(A)
LIST_M = []
for _ in range(M):
    A = input()
    LIST_M.append(A)

count = 0
for DATA in LIST_M:
    if (DATA in SET_N) == True:
        count += 1

print(count)

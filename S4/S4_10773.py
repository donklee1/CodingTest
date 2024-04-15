# S4_10773 스택사용
K = int(input())
L = [] # STACK
for _ in range(K):
    N = int(input())
    if N != 0:
        L.append(N)
    else: # 0인경우는 최근것 제거
        L.pop()

print(sum(L))

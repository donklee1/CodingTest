K = int(input())
L = [] # STACK
for _ in range(K):
    N = int(input())
    if N != 0:
        L.append(N)
    else:
        L.pop()

print(sum(L))

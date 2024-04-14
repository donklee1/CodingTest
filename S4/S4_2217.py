import sys
N = int(input())
L = []
for i in range(N):
    L.append(int(input()))

L.sort(reverse=True)

max_val = 0
for i in range(N):
    weight = L[i]
    max_val = max(max_val, weight * (i+1))

print(max_val)    


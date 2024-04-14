# 24060
from sys import stdin

k_count = 0
k_val = -1
def merge(A, p, q, r):
    global K
    global k_count
    global k_val
    i = p
    j = q + 1
    t = 0
    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp[t] = A[i] # tmp[t] <- A[i]; t++; i++;
            t += 1
            i += 1
        else:
            tmp[t] = A[j] # tmp[t] <- A[j]; t++; j++;
            t += 1
            j += 1

    while (i <= q):  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        t += 1
        i += 1
    while (j <= r):  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        t += 1
        j += 1
    i = p
    t = 0
    while (i <= r):  # 결과를 A[p..r]에 저장
        A[i] = tmp[t]; 
        k_count += 1
        if (k_count == K):
            k_val = A[i]
        i += 1
        t += 1

def merge_sort(A, p, r): # A[p..r]을 오름차순 정렬한다.
    if (p == r):
        return
    if (p < r):
        q = (p + r) // 2       # q는 p, r의 중간 지점
        merge_sort(A, p, q)     # 전반부 정렬
        merge_sort(A, q + 1, r) # 후반부 정렬
        merge(A, p, q, r)        # 병합

N, K = map(int, input().split())
L = list(map(int, input().split()))
#N, K = map(int, "5 13".split())
#L = list(map(int, "4 5 1 3 2".split()))
tmp = [0 for _ in range(N)]
merge_sort(L, 0, len(L)-1)
print(k_val)

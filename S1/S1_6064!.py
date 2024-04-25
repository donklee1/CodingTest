# S1_6064 카잉달력
from sys import stdin

def Kaing_year(M, N, x, y):
    k = x
    while k <= M*N:
        #if k % N == y: 에러발생 (x==M이거나 y==N이면, 성립안함)
        if (k - y) % N == 0:
            return k
        k += M
 
    return -1

T = int(input())
for _ in range(T):
    M, N,x,y = map(int, input().split())
    year = Kaing_year(M,N,x,y)
    print(year)

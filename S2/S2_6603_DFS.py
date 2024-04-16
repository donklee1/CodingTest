# S2_6603 K개의 수중에서 6개를 고르는 조합모두 출력
from sys import stdin

RESULT = []

def DFS(K, start):
    if len(RESULT) == 6: # 6개을 고르는 경우
        print(*RESULT) #리스트를 공백으로 출력하는 방법
        return
    
    for i in range(start, K):
        RESULT.append(DATA[i])
        DFS(K, i+1)
        RESULT.pop()
            

while True:
    DATA = list(map(int, stdin.readline().split()))
    K = DATA[0] # 데이터 길이
    DATA.pop(0) # 길이값 제거
    DATA.sort() # 정렬
    RESULT = []
    DFS(K, 0)
    print("")
    if K == 0: # 마지막 데이터
        break

# 1182 S2
import itertools

N, S = map(int,input().split())
DATA = list(map(int,input().split()))

cnt = 0

def dfs(index, SUM):
	global cnt
	if index >= N:
		return
	SUM += DATA[index]
	if SUM == S:
		cnt += 1

	dfs(index+1, SUM)              # 해당윈소를 사용하는 경우
	dfs(index+1, SUM-DATA[index])  # 해당윈소를 사용하지 않는 경우

def comb_solution(N):
	global cnt
	for k in range(1, N+1):
		for comb in itertools.combinations(DATA, k):
		    if sum(comb) == S:
			    cnt += 1

dfs(0,0) # 280ms
#comb_solution(N) # 272ms
print(cnt)
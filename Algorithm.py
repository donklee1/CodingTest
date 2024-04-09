# Algorithm.py
# 랜덤추천문제 : https://devjeong.com/algorithm/algorithm-1/

# ----- 1. DFS -----
#
#  DFS1 : 스택을 사용하는 경우: 항목출력요구
#  <15649 S3> 1~N 사이의 M개의 숫자조합 출력 (중복없음) nPr
#  <15650 S3> 1~N 사이의 M개의 숫자조합 출력 (오름차순)
#  <15651 S3> 1~N 사이의 M개의 숫자조합 출력 (중복가능) nCr
#  <15652 S3> 1~N 사이의 M개의 숫자조합 출력 (비내림차순)
#  <14888 S1> 연산자 끼워넣기 (내부루프는 연산자 조합)
RESULT_STACK = []
def DFS1(N, M):
    # 모든항목 조건만족 경우
    if len(RESULT_STACK) == M:
        # 정답(목록) 출력
        return

    for i in range(1, N+1): # 모든경우 루프
        if (i in RESULT_STACK) == False: # 1항목 <조건>만족
            RESULT_STACK.append(i) # 추가
            DFS1() # 내부심화 탐색
            RESULT_STACK.pop() # BackTracking

#  DFS2 : 스택미사용, 행과열 루프
#  <9663 G4> N-Queen (결과-개수)
# 행,열에 대한 루프를 진행 (열은 내부 for/ 행은 DFS 인수)
def DFS2(N, row): # ---- 스택 미사용 경우 ---
    # 모든항목 조건만족 경우
    if row == N:
        # 처리
        return

    for col in range(N): # 열에대한 루프
        # 조건을 검색하여 만족하는 경우
        # 데이터를 체크 (push와 같은 기능)
        DFS2(N, row+1) # 다음행에 대한 진행
        # 데이터를 언체크 (pop와 같은 기능)

#  DFS3 : 스택미사용, 특수 조건루프
#  <2580 G4> 스도쿠 (빈칸계산)
def DFS3(count, MAX):
    if count == MAX:
        # 조건처리
        return
    for val in range(1, 10): #특수조건
        if val == 4: # 조건만족하는 경우
            # 데이터를 체크 (push와 같은 기능)
            DFS2(count+1, MAX) # 다음행에 대한 진행
            # 데이터를 언체크 (pop와 같은 기능)

# DFS4 : 중복을 허용하지 않는 조합에 대하여 각항목의 포함여부 테크닉
DATA = list(map(int,input().split()))
def DFS4(index, SUM):
    # 조건만족 판단

	DFS4(index+1, SUM)              # 해당윈소를 사용하는 경우
	DFS4(index+1, SUM-DATA[index])  # 해당윈소를 사용하지 않는 경우


# ----- 2. DP -----
# 부분결과를 저장하는 배열이 필요함
# DP1 : 초기항 값 --> 점화식에 의한 순방향 계산 !!
#  - 수동으로 첫항부터 값을 나열해본다 (4~5개) --> 점화식 유추
#  - 피보나치 수열(24416) , 01타일문제(1904), 파도반수열(9416) 문제등..
# DP2 : 최소값, 최대값 계산
#  - 배열에 각 단계에서 이전단계를 고려한 max(), min() 함수로 단계의 최대,최소값을 계산 (이부분이 어렵다)
#  - 지붕칠하기(1149)
#  - 역방향으로 생각해야 하는 경우 존재함 (어렵다) 
# DP3 : 딕셔너리에 k-val 값을 저장하고, 두번계산하지 않고 결과를 사용함

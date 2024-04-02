# Algorithm.py

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
def DFS2(N, row): # ---- 스택 미사용 경우: 항목출력요구 ---
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

# ----- 2. DP -----

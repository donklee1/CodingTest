# S4_1620 : 포켓몬 검색 (양방향 dict)
from sys import stdin
P_COUNT, QUREY_COUNT = map(int, input().split())

POKET_DICT  = dict() # 딕셔너리 정의 (숫자 -->"이름")
POKET_DICT2 = dict() # 딕셔너리 정의 ("이름" -->숫자)
for i in range(1,P_COUNT+1):
    NAME = stdin.readline().rstrip()  # 속도향상
    POKET_DICT[i] = NAME # 딕셔너리 입력
    POKET_DICT2[NAME] = i # 딕셔너리 입력

for _ in range(QUREY_COUNT):
    QUESTION = stdin.readline().rstrip() # 속도향상
    if QUESTION.isdigit(): # 숫자판단
        RES = POKET_DICT.get(int(QUESTION))
        print(RES)
    else: # 문자
        RES = POKET_DICT2.get(QUESTION)
        print(RES)
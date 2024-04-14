# 20920
from sys import stdin
N, M = map(int, input().split()) # 단어개수, 기준단어 길이

DICT_WORD = {}
for _ in range(N):
    WORD = stdin.readline().rstrip()
    if len(WORD) < M:
        continue
    if (WORD in DICT_WORD) == False:
        DICT_WORD[WORD] = [1, len(WORD), WORD] # 단어가 존재하지 않는경우
    else:
        DICT_WORD[WORD][0] += 1

RESULT_LIST = sorted(DICT_WORD.items(), key = lambda x:(-x[1][0], -x[1][1], x[1][2]))
# -x[1][0] -- 빈도(내림차순),  -x[1][1] -- 길이(내림차순), x[1][2] 알파벳(오름차순)
# --> 결과 list of dict

for dict_item in RESULT_LIST:
    print(dict_item[0]) # key = 단어
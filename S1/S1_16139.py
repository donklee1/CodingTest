from sys import stdin
S = input().rstrip()
SLIST = list(S)
LEN = len(S)

# --- 26개의 알파벳에 대하여 한꺼번에 계산
SUMLIST = [[0] * LEN for _ in range(26)]
for a_index in range(0, 26): # a,b,c, ..
    count = 0
    alpha = chr(ord('a') + a_index)
    for i in range(LEN):
        if SLIST[i] == alpha:
            count += 1
        SUMLIST[a_index][i] = count
#print(SUMLIST)

Q = int(input()) # 질문수
for _ in range(Q):
    alpha, l_str, r_str = stdin.readline().split()
    a_index = ord(alpha) - ord('a')
    l = int(l_str)
    r = int(r_str)

    if l == 0:
        RESULT = SUMLIST[a_index][r]
    else:
        RESULT = SUMLIST[a_index][r] - SUMLIST[a_index][l-1]
    print(RESULT)

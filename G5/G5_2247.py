# 2447 번
def TriPattern(H_START, V_START, N):
    global PAT
    
    # --- 가운데 구멍 ---
    #print("N=", N, "H_START=", H_START, "V_START=", V_START)
    if N == 3:
        PAT[H_START + 1][V_START + 1] = " "
        return
    else:
        LEN = N // 3 # 3등분
        v1 = V_START + LEN
        h1 = H_START + LEN
        h2 = H_START + LEN * 2
        v2 = V_START + LEN * 2
        for i in range(h1, h2):
            for j in range(v1, v2):
                PAT[i][j] = " "

    TriPattern(H_START, V_START, N // 3)
    TriPattern(H_START, V_START+LEN, N // 3)
    TriPattern(H_START, V_START+LEN*2, N // 3)

    TriPattern(H_START+LEN, V_START, N // 3)
    TriPattern(H_START+LEN, V_START+LEN*2, N // 3)

    TriPattern(H_START+LEN*2, V_START, N // 3)
    TriPattern(H_START+LEN*2, V_START+LEN, N // 3)
    TriPattern(H_START+LEN*2, V_START+LEN*2, N // 3)

N = int(input())  # 3의 거듭제곱 (지수로 착각)
PAT = [["*" for i in range(N)] for j in range(N)]
TriPattern(0, 0, N)
for i in range(N):
    print(''.join(PAT[i]))

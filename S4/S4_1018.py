N, M = map(int, input().split()) # 행, 열
WB_LIST = [["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"]]
BW_LIST = [["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"],
           ["B", "W", "B", "W", "B","W", "B","W"],
           ["W", "B", "W", "B","W", "B","W", "B"]]

NM_LIST = [["a" for j in range(M)] for i in range(N)]
for i in range(N):
    NM_LIST[i] = list(input()) #행단위 복사

min_change1 = 65
for i in range(N-7):
    for j in range(M-7):
        change = 0
        for k in range(8):
            for m in range(8):
                if NM_LIST[i+k][j+m] != WB_LIST[k][m]:
                    change += 1
        if change < min_change1:
            min_change1 = change

min_change2 = 65
for i in range(N-7):
    for j in range(M-7):
        change = 0
        for k in range(8):
            for m in range(8):
                if NM_LIST[i+k][j+m] != BW_LIST[k][m]:
                    change += 1
        if change < min_change2:
            min_change2 = change

print(min(min_change1,min_change2))

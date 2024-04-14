def Cantor(L, A, B):
    #print(L, A, B)
    LEN = (B - A) // 3
    if LEN < 1:
        return
    # 중간을 지운다
    d1 = A + LEN
    d2 = B - LEN
    for i in range(d1, d2):
        L[i] = " "

    Cantor(L, A, d1) # 앞부분 1/3
    Cantor(L, d2, B) # 뒷부분 1/3

while True:
    try:
        N = int(input())
        L = ["-" for i in range(3 ** N)]
        Cantor(L, 0, len(L))
        for a in L:
            print(a, end='')
        print("")
    except:
        break

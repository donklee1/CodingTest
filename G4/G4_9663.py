# 9663 N-Queen G4

def CheckRow(row):
    return (HORZ[row] == False)

def CheckCol(col):
    return (VERT[col] == False)

def CheckDiag1(row, col): # /
    index = row + col
    return (DIAG1[index] == False)

def CheckDiag2(N, row, col): # \
    index = col + (N-row-1)
    return (DIAG2[index] == False)

def DFS(N, row):
    global count
    if row == N:
        count += 1
        return
    for col in range(N):
        if CheckRow(row) and CheckCol(col) and CheckDiag1(row, col) and CheckDiag2(N, row, col):
            HORZ[row] = True
            VERT[col] = True
            DIAG1[row+col] = True
            DIAG2[col + (N-row-1)] = True
            DFS(N, row+1)
            HORZ[row] = False
            VERT[col] = False
            DIAG1[row+col] = False
            DIAG2[col + (N-row-1)] = False

# -----------------------------------------------
N = int(input())
HORZ = [False] * N
VERT = [False] * N
DIAG1 = [False] * (N+N-1) # /
DIAG2 = [False] * (N+N-1) # \
count = 0
DFS(N, 0)
print(count)
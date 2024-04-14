# 11729 G5 - Hanoi

def Hanoi(N, src, dest, via):
    global move_count
    global L
    if N == 1:
        move_count += 1
        L.append((src, dest))
        return
    Hanoi(N-1, src, via, dest) # N-1개를 보조로 옮김
    
    move_count += 1
    L.append((src, dest)) # 가장큰것(하단)을 목적지로 이동

    Hanoi(N-1, via, dest, src) # N-1개를 보조에서 목적지로 옮김

# --------------------------------------
N = int(input())
move_count = 0
L = []
Hanoi(N, 1, 3, 2)
print(move_count)
for (a, b) in L:
    print(a, b)

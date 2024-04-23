# S1_2718 미로탐색
from sys import stdin
import sys

row_count, column_count = map(int, stdin.readline().split())
dest_x = column_count - 1
dest_y = row_count - 1
PUZZLE = []
for i in range(row_count):
    PUZZLE.append(list(map(int, stdin.readline().rstrip())))

def DFS(y, x, pass_count):
    global min_count
    global dest_x, dest_y
    if (x < 0) or (y < 0) or (x > dest_x) or (y > dest_y):
        return
    if (Visited[y][x] == 1) or (PUZZLE[y][x] == 0):
        return
    print("DEF",y,x, pass_count)
    Visited[y][x] = 1
    if (y == dest_y) and (x == dest_x):
        print("--> min",y,x, pass_count)
        min_count = min(min_count, pass_count)
        return
    
    DFS(y-1, x, pass_count+1)
    DFS(y+1, x, pass_count+1)
    DFS(y, x+1, pass_count+1)
    DFS(y, x-1, pass_count+1)

min_count = 10e9
Visited = [[0] * column_count for _ in range(row_count)]
DFS(0,0, 1)
print(min_count)

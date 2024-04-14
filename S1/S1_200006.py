# 20006 S1 랭킹전대기열
from sys import stdin

player_count, room_capacity = map(int, stdin.readline().split())
WAIT_LIST = []
for i in range(player_count):
    level, name = stdin.readline().split()
    WAIT_LIST.append((int(level), name))

GAME_ROOMS = []

def InsertNewRoom(level, name):
    GAME_ROOM = []
    GAME_ROOM.append((level, name))
    GAME_ROOMS.append(GAME_ROOM)

for i in range(player_count):
    (level, name) = WAIT_LIST[i]
    Inseted = False
    for k in range(len(GAME_ROOMS)):
        GAME_ROOM = GAME_ROOMS[k]
        (first_level, first_name) = GAME_ROOM[0]
        if (len(GAME_ROOMS[k]) < room_capacity) and ((first_level - 10) <= level) and (level <= (first_level + 10)):
            GAME_ROOMS[k].append((level, name))
            Inseted = True
            break
    if (Inseted == False):
        InsertNewRoom(level, name)

for k in range(len(GAME_ROOMS)):
    if len(GAME_ROOMS[k]) == room_capacity:
        print("Started!")
    if len(GAME_ROOMS[k]) < room_capacity:
        print("Waiting!")
    GAME_ROOMS[k].sort(key=lambda x : x[1])
    for (l, n) in GAME_ROOMS[k]:
        print(l, n)

# 2852 S3 NBA 농구
from sys import stdin

def StringToSec(STR):
    min, sec = map(int, STR.split(":"))
    return min * 60 + sec
def SecToString(total_sec):
    min = total_sec // 60
    sec = total_sec % 60
    return str(min).zfill(2) + ":" + str(sec).zfill(2)

SCORE = [0,0]
win_team = -1
SCORE_TIME = [0]
WIN_TIME = [0,0]
gole_count = int(stdin.readline().strip())
for _ in range(gole_count):
    team_str, time_str = stdin.readline().split()
    time_val = StringToSec(time_str)
    SCORE_TIME.append(time_val)
    goal_team = int(team_str) - 1

    if (win_team != -1): # 스코어 이전의 이긴팀 점수계산
        WIN_TIME[win_team] += (time_val - SCORE_TIME[-2])

    SCORE[goal_team] += 1
    if SCORE[0] > SCORE[1]:
        win_team = 0
    elif SCORE[1] > SCORE[0]: 
        win_team = 1
    else:
        win_team = -1

# --- 나머지 시간계산
if win_team != -1:
    WIN_TIME[win_team] += (48*60 - SCORE_TIME[-1])        
 
print(SecToString(WIN_TIME[0]))
print(SecToString(WIN_TIME[1]))
# S4_26069 총총이 
N = int(input())
CAN_DANCE = {"ChongChong"} # 중복제거를 위해 집합사용
for _ in range(N):
    NAME1, NAME2 = input().split()
    if NAME1 in CAN_DANCE:
            CAN_DANCE.add(NAME2)
    if NAME2 in CAN_DANCE:
            CAN_DANCE.add(NAME1)

print(len(CAN_DANCE))

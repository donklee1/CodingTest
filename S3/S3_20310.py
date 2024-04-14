# 20310 S3 
from sys import stdin

S = stdin.readline().rstrip()
str_length = len(S)
Removed = [False] * str_length
zero_count = S.count("0") // 2
one_count = S.count("1") // 2

# 전략: 가능하면 앞부분의 1을 지우고, 가능하면 뒷부분의 0을 지워야 한다
for i in range(str_length): # --> 방향으로 1을 제거
    if one_count > 0 and S[i] == "1":
        Removed[i] = True
        one_count -= 1

for i in range(str_length-1, -1, -1): # <-- 방향으로 0을 제거
    if zero_count > 0 and S[i] == "0":
        Removed[i] = True
        zero_count -= 1

result = ""
for index, remove_item in enumerate(Removed):
    if remove_item == False:
        result += S[index]

print(result)        

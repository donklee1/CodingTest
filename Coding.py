# 21314 S1
from sys import stdin

S = stdin.readline().strip()

# --- Token 분리 ---
token = []
sub_str = ""
for s1 in S:
    if s1 != "K":
        sub_str += s1
    else:
        sub_str += "K"
        token.append(sub_str)
        sub_str = ""
if (sub_str != ""):
    token.append(sub_str)

min_str = ""
max_str = ""
for tok in token:
    m_count = str(tok).count("M")
    print("tok=", tok)
    if "K" in tok: # MMMMMK 타입
        if m_count == 0:
            max_str += "5"
            min_str += "5"
        else:
            max_str += str(5 * (10 ** m_count)) # 500..
            min_str += str((10 ** m_count) + 5) # 100.. 5
    else: # MMMMM 타입
        max_str += str(('1' * m_count))
        min_str += str(10 ** (m_count-1))

print(max_str)
print(min_str)

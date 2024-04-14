# 22233 S2 : 가희와 키워드
from sys import stdin

keyword_dict = {}
keywords, notes = map(int, stdin.readline().split())
for i in range(keywords):
    keyword = stdin.readline().rstrip()
    keyword_dict[keyword] = i

for i in range(notes):
    keylist = list(stdin.readline().rstrip().split(","))
    for key in keylist:
        if key in keyword_dict:
            del keyword_dict[key]
    print(len(keyword_dict))

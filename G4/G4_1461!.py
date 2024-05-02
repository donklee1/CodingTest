# G4_1461 도서관

N, M = map(int, input().split())
BOOK = list(map(int, input().split()))
BOOK_PLUS = []
BOOK_MINUS = []
max_dist = 0
for pos in BOOK:
    # 돌아오지 않아도될 가장먼것
    max_dist = max(abs(pos), max_dist)
    if pos < 0:
        BOOK_MINUS.append(pos)
    elif pos > 0:
        BOOK_PLUS.append(pos)

BOOK_PLUS.sort(reverse=True)
BOOK_MINUS.sort()

total_dist = 0
for p in range(0, len(BOOK_PLUS), M):
    total_dist += abs(BOOK_PLUS[p]) * 2 #멀리갔다 원점복귀

for p in range(0, len(BOOK_MINUS), M):
    total_dist += abs(BOOK_MINUS[p]) * 2 #멀리갔다 원점복귀

print(total_dist - max_dist) #돌아오지 않을거리를 하나빼줌
        



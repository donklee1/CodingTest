from sys import stdin
NoHear = set()
NoSee = set()

#HEAR = ["ohhenrie", "charlie", "baesangwook"]
#SEE = ["obama", "baesangwook", "ohhenrie", "clinton"]

N, M = map(int, input().split())
#N, M = map(int, "3 4".split())
for i in range(N):
    NAME = stdin.readline().rstrip()
    #NAME = HEAR[i]
    NoHear.add(NAME)
for i in range(M):
    NAME = stdin.readline().rstrip()
    #NAME = SEE[i]
    NoSee.add(NAME)


NoHearSee = NoHear & NoSee # 교집합
RESULT = list(NoHearSee)    
RESULT.sort()

count = len(RESULT)
print(count)
for i in range(count):
    print(RESULT[i])

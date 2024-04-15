# 17219 S4
from sys import stdin

site_count, qurey_count = map(int, stdin.readline().split())
SITE = {} # dict 

for _ in range(site_count):
    site, password = stdin.readline().split()
    SITE[site] = password

for _ in range(qurey_count):
    site = stdin.readline().rstrip()
    print(SITE[site])

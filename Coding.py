from sys import stdin
import re

S = 'apple orange:banana,tomato'
L = re.split('[ ,:]', S)
L2 = re.split('([ ,:])', S)
print(L)
print(L2)


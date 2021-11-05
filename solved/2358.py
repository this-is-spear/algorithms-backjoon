# dx = []
# dy = []
# for i in range(int(input())):
#     a, b = map(int, input().split())
#     dx.append(a)
#     dy.append(b)
# import collections
# xx = collections.Counter(dx).items()
# yy = collections.Counter(dy).items()
#
# print(sum([1 for i in xx if i[1] >= 2]) + sum([1 for i in yy if i[1] >= 2]))


import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

coordX = defaultdict(int)
coordY = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    coordX[x] += 1
    coordY[y] += 1

answer = sum(n > 1 for _, n in coordX.items()) + sum(n > 1 for _, n in coordY.items())
print(answer)
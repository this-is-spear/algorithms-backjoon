import sys

for _ in range(int(sys.stdin.readline())):
    an = 1
    a = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        i, k = map(int, sys.stdin.readline().split())
        a.append((i, k))
    a.sort()
    Max = a[0][1]
    for i in range(n):
        if Max > a[i][1]:
            an += 1
            Max = a[i][1]
    print(an)
import math
for _ in range(int(input())):
    di = {}
    for _ in range(int(input())):
        a,b = input().split()
        di.setdefault(b, 1)
        di[b] += 1
    print(math.prod(di.values(), start=1) - 1)
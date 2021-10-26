import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
res = -1
que = deque([(a, 1)])
while que:
    i, cnt = que.popleft()
    if i == b:
        res = cnt
        break
    if i * 2 <= b:
        que.append((i * 2, cnt + 1))
    if int(i * 10 + 1) <= b:
        que.append((i*10 + 1, cnt + 1))
print(res)

import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
arr = [[0] * m for _ in range(n)]
deque = deque([])
for i in range(n):
    temp = list(map(int, input().split()))
    for k in range(m):
        if temp[k] == 1:
            deque.append([[i, k], 0])
            arr[i][k] = 1
        elif temp[k] == -1:
            arr[i][k] = 1
last_day = 0

while deque:
    item = deque.popleft()
    last_day = item[1]
    # 상
    if item[0][1] > 0:
        if arr[item[0][0]][item[0][1] - 1] == 0:
            arr[item[0][0]][item[0][1] - 1] = 1
            deque.append([[item[0][0], item[0][1] - 1], item[1] + 1])
    # 하
    if item[0][1] < m - 1:
        if arr[item[0][0]][item[0][1] + 1] == 0:
            arr[item[0][0]][item[0][1] + 1] = 1
            deque.append([[item[0][0], item[0][1] + 1], item[1] + 1])

    # 좌
    if item[0][0] > 0:
        if arr[item[0][0] - 1][item[0][1]] == 0:
            arr[item[0][0] - 1][item[0][1]] = 1
            deque.append([[item[0][0] - 1, item[0][1]], item[1] + 1])
    # 우
    if item[0][0] < n - 1:
        if arr[item[0][0] + 1][item[0][1]] == 0:
            arr[item[0][0] + 1][item[0][1]] = 1
            deque.append([[item[0][0] + 1, item[0][1]], item[1] + 1])

answer = sum([sum(i) for i in arr])
if answer == m * n:
    print(last_day)
else:
    print(-1)
